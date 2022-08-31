import os
import json
import shutil
import zipfile
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import pkcs7, pkcs12, Encoding

def signpass(pass_dir, wwdr_path, cert_path, password, output):
    # Load Pass Type ID Certificate and private key from .p12 file
    with open(cert_path, 'rb') as cert_file:
        key, cert, _ = pkcs12.load_key_and_certificates(cert_file.read(),  password.encode('utf-8'))
        #cert_itself = x509.load_der_x509_certificate(cert_file.read())
    # Load Apple WWDR certificate 
    with open(wwdr_path, 'rb') as wwdr_file:
        wwdr = x509.load_der_x509_certificate(wwdr_file.read())

    # Make list all files in the pass folder
    filelist = []
    for root, _, files in os.walk(pass_dir):
        for file in files:
            if not file.startswith("."): # ignore hidden files
                filelist.append(os.path.join(root, file))
            if os.path.basename(file) == ".DS_Store":
                os.remove(os.path.join(root, file))

    # Calculate SHA1 hash of each file in the pass folder
    file_hashes = {}
    for file in filelist:
        hasher = hashes.Hash(hashes.SHA1())
        with open(file, 'rb') as asset:
            bytes = asset.read()
            hasher.update(bytes)
            file_hashes[os.path.relpath(file, pass_dir)] = hasher.finalize().hex() 

    # Write the file hashes to a JSON file in the same directory
    with open(os.path.join(pass_dir, "manifest.json"), 'w') as manifest:
        json.dump(file_hashes, manifest, indent=2)

    # Read manifest file into a byte array
    with open(os.path.join(pass_dir, "manifest.json"), 'rb') as manifest:
        payload = manifest.read()

    # Set options for signature
    options = [pkcs7.PKCS7Options.DetachedSignature, pkcs7.PKCS7Options.Binary]

    # Perform signature
    signature = pkcs7.PKCS7SignatureBuilder().set_data(
        payload
    ).add_signer(
        cert, key, hashes.SHA256()
    ).add_certificate(
        wwdr
    ).sign(
        Encoding.DER, options
    )
    
    # Write signature to file
    with open(os.path.join(pass_dir, "signature"), 'wb') as sig_file:
        sig_file.write(signature)

    # Compress the directory
    """
    for root, _, files in os.walk(pass_dir):
        for file in files:
            if not file.startswith("."): # ignore hidden files
                zip.write(os.path.join(root, file), 
                    os.path.relpath(file, pass_dir))
    
    with zipfile.ZipFile(output + ".zip", 'w') as zip:
        for root, _, files in os.walk(pass_dir):
            for file in files:
                if not file.startswith("."): # ignore hidden files
                    print(os.path.join(root, file))
                    zip.write(os.path.join(root, file), 
                    os.path.relpath(file, root))
    """
    os.mkdir(output)
    shutil.copytree(pass_dir, output, dirs_exist_ok=True)
        
    # Rename to pkpass
    #os.rename(output + ".zip", output + ".pkpass")
def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)