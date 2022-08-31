#!/usr/bin/env python3
import os
import shutil
import tempfile
import argparse
from signpass import signpass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pass_dir', type=str, help="Path to the .pass directory")
    parser.add_argument('--wwdr', type=str, required=True, help="Path to Apple WWDR certificate")
    parser.add_argument('--cert', type=str, required=True, help="Path to Pass Type ID Certificate")
    parser.add_argument('--pwd', type=str, help="Password for private key")
    args = parser.parse_args()
    src = args.pass_dir
    
    with tempfile.TemporaryDirectory() as dst:
        newdir = os.path.join(dst, os.path.basename(src))
        print(newdir)
        os.mkdir(newdir)
        shutil.copytree(src, newdir, dirs_exist_ok=True)
        signpass(newdir, args.wwdr, args.cert, args.pwd, "./HillelPass")


if __name__ == "__main__":
    main()
