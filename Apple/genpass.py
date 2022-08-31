#!/usr/bin/env python3
import os
import sys
import json
import shutil
import tempfile
import subprocess

def main():
    num_args = len(sys.argv)
    if num_args == 3:
        print("should read from file")
    elif num_args == 5:
        pass_dir = sys.argv[1]
        name = sys.argv[2]
        uid = sys.argv[3]
        barcode = sys.argv[4]
        makepass(pass_dir, name, uid, barcode)
    else:
        print("Invalid arguments")
        return
    
def makepass(pass_dir, name, uid, barcode):
    if len(uid) != 9:
        print("UID must be 9 digits")
        return
    if len(barcode) != 14:
        print("Barcode must be 14 digits")
        return
    try:
        os.remove(os.path.join(pass_dir, ".DS_Store"))
    except OSError:
        pass
    # Make temp directory to make pass in
    with tempfile.TemporaryDirectory() as dst:
        just_folder = os.path.basename(pass_dir)
        newdir = os.path.join(dst, just_folder)
        os.mkdir(newdir)
        # copy pass source to temp directory
        shutil.copytree(pass_dir, newdir, dirs_exist_ok=True) 
        # open pass.json
        with open(os.path.join(newdir, "pass.json"), "r") as pass_file:
            data = json.load(pass_file)
            # write custom data to json object
            data['serialNumber'] = uid
            data['generic']['secondaryFields'][0]['value'] = uid
            data['generic']['primaryFields'][0]['value'] = name
            for code in data['barcodes']:
                code['message'] = barcode
                code['altText'] = barcode
        
        with open(os.path.join(newdir, "pass.json"), "w") as pass_file:
            json.dump(data, pass_file)
        
        subprocess.run(["./signpass", "-p", newdir]) # run pass signer tool
        shutil.move(os.path.join(dst, f"{os.path.splitext(just_folder)[0]}.pkpass"), 
                        f"./{uid}.pkpass") # copy created pass back to current directory

if __name__ == "__main__":
    main()
