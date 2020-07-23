# import packages
import snowflake.connector as sc
import numpy as np
from googleapiclient import discovery
from oauth2client import file, client, tools

# Get data from google sheets
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def get_credentials():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    return creds

creds = get_credentials()

service = discovery.build('sheets', 'v4', credentials=creds)

ssId = '' # insert Sheet ID here
wsRespRange = '' # insert sheet range here

request = service.spreadsheets().values().batchGet(spreadsheetId=ssId, ranges=wsRespRange)
response = request.execute()

# Create Query
query = '' + sNums

# Connect to snowflake run query
user = '' # insert snowflake user name
password = '' # insert snowflake password
account = '' # insert snowflake account

cnx = sc.connect(
        user=user,
        password=password,
        account=account)

snowResponse = cnx.cursor().execute(query)
cnx.close()
result = np.asarray([[x[0] for x in snowResponse.description]] + list(snowResponse)).tolist()

# clear range 
range = '' # range to clear
service.spreadsheets().values().clear(spreadsheetId=ssId, range=range).execute()

# populate query data to google sheet
wsDataRange = range + str(len(result))
data = { 'range': wsDataRange, 'values': result }
body = { 'valueInputOption': 'USER_ENTERED', 'data': data }

service.spreadsheets().values().batchUpdate(spreadsheetId=ssId, body=body).execute()