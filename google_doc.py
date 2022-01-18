from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.

def get_service(scopes):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('docs', 'v1', credentials=creds)

service = get_service(['https://www.googleapis.com/auth/documents'])

def get_document(document_id):
    # Retrieve the documents contents from the Docs service.
    return service.documents().get(documentId=document_id).execute()


template = ""
TEMPLATE_ID = "1xdGwEkjGpa_vpUrHeNTMW1i-Y1B-JGEsILp5csKrhvQ"
DIARIO_ID = "1bjIb_jFMhLTlWaECKigocE63o8HIhH-ObkWK5kCwPXk"

document_template = get_document(TEMPLATE_ID)
document_diario = get_document(DIARIO_ID)

""
def get_element(doc):
    if 'paragraph' in doc:
        for element in doc['paragraph']['elements']:



#for child in document_template:
#document_diario = get_document(DIARIO_ID)

service = get_service(['https://www.googleapis.com/auth/documents'])
result = service.documents().batchUpdate(
    documentId=DIARIO_ID,
    body={
        'requests': [
            get_element(doc_line) for doc_line in document_template['body']['content']
        ]
    }
).execute()
