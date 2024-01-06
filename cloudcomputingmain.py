# -*- coding: utf-8 -*-
"""CloudComputingMain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_uLgyHv7tTEGNxsdEQtti1cc_H_zL6PF
"""

pip install pyminizip

import pyminizip
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/content/service_api.json'

PARENT_FOLDER_ID = "16ZvRpj46VDYq_QldkWtRUZPeD4FEiRoa"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
def encryptionn(outp):
    inpt = input("Enter file to be secured: ")
    pref = None
    filnm = input("Enter filename: ")
    outp = "./"+filnm+".zip"
    ch = int(input("Do you want custom password/default password ?(1/0): "))
    pwdd = None
    if ch == 1:
        pwdd = input("Enter Custom Password: ")
    pwd = "abc"
    comp_lv = 5
    if pwdd is not None:
        pyminizip.compress(inpt, pref, outp, pwdd, comp_lv)

    else:
        pyminizip.compress(inpt, pref, outp, pwd, comp_lv)
    return outp
upload(encryptionn(outp))

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/ar646/Desktop/Proj/CloudComputing/service_api.json'
PARENT_FOLDER_ID = "16ZvRpj46VDYq_QldkWtRUZPeD4FEiRoa"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()


upload("test.zip")