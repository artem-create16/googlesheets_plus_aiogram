import apiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from data import config


def get_sheet_values(diapason):
    credentials_file = "work_with_sheet/creds.json"
    spreadsheet_id = config.SPREADSHEET_ID

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=diapason,
        majorDimension='ROWS'
    ).execute()
    try:
        main_values = values['values']
        string_with_values = ''
        for num, value in enumerate(main_values):
            one_string = f"{num + 1}. {value[0]} - {value[1]}\n"
            string_with_values += one_string
        return string_with_values

    except KeyError:
        return 'That is all'
