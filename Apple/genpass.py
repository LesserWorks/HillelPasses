#!/usr/bin/env python3
import os
import sys
import json
import shutil
import openpyxl
import tempfile
import subprocess

def main():
    num_args = len(sys.argv)
    if num_args == 4:
        pass_dir = sys.argv[1]
        xlsx = sys.argv[2]
        dest = sys.argv[3]
        dest_path = os.path.join("./", dest)
        if os.path.exists(dest_path) and os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
        os.mkdir(dest_path)
        workbook = openpyxl.load_workbook(xlsx)
        worksheet = workbook.active
        for row in worksheet.iter_rows(2, worksheet.max_row, values_only=True):
            name = " ".join([row[0], row[1]])
            id = str(row[2])
            barcode = str(row[3])
            makepass(pass_dir, name, id, barcode, os.path.join(dest_path, f"{name.replace(' ', '')}.pkpass"))


            
    elif num_args == 5:
        pass_dir = sys.argv[1]
        name = sys.argv[2]
        uid = sys.argv[3]
        barcode = sys.argv[4]
        makepass(pass_dir, name, uid, barcode, f"./{uid}.pkpass")
    else:
        print("Invalid arguments")
        return
    
def makepass(pass_dir, name, uid, barcode, dest):
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
        shutil.move(os.path.join(dst, f"{os.path.splitext(just_folder)[0]}.pkpass"), dest) # copy created pass back to current directory

if __name__ == "__main__":
    main()
