import os
import time
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from helper_functions import read_yaml

config = read_yaml("./config.yaml")

credential_file = config['DRIVE']['credentials_file']

# Define your Google Drive API credentials
credentials = service_account.Credentials.from_service_account_file(credential_file)
drive_service = build('drive', 'v3', credentials=credentials)

# Define the directory path where the files are located
directory_path = config['DRIVE']['screenshot_folder']

# Define the Google Drive folder ID where the files will be uploaded
folder_id = config['DRIVE']['folder_id']


def upload_file(file_path):
    file_name = os.path.basename(file_path)
    media = MediaFileUpload(file_path)

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File uploaded: {file_name} (ID: {file["id"]})')


def main():
    while True:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                upload_file(file_path)
                time.sleep(30)


if __name__ == '__main__':
    main()
