import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the credentials JSON file downloaded
creds = service_account.Credentials.from_service_account_file('C:/Users/ar646/Desktop/Proj/CloudComputing/api_login.json')

# Create a Drive API service
drive_service = build('drive', 'v3', credentials=creds)

# Example: List all files in Drive
results = drive_service.files().list(pageSize=10).execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f"{item['name']} ({item['id']})")
