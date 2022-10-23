#!/usr/bin/env python3
import os
import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Generate download links for all files in a Google folder")
    parser.add_argument('--key', type=str, required=True, help="API key enabled for Google Drive API from Google Cloud console")
    parser.add_argument('--folder-url', type=str, required=True, help="URL of folder containing the files")
    args = parser.parse_args()
    key = args.key
    folder = os.path.basename(args.folder_url)
    url = f"https://www.googleapis.com/drive/v3/files?fields=files(name,id)&key={key}&q=%27{folder}%27%20in%20parents&orderBy=name&pageSize=1000"
    response = requests.get(url)
    data = response.json()
    for file in data['files']:
        print(os.path.splitext(file['name'])[0])

    for file in data['files']:
        print(f"https://drive.google.com/uc?export=download&id={file['id']}")


if __name__ == "__main__":
    main()
