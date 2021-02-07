import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet_values(diapason):
    credentials_file = "work_with_sheet/creds.json"
    spreadsheet_id = '1NlnA0DQYD9A-SfRK-WtCtxtQmV9EZsoJq98gGNpQWVM'

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
    main_values = values['values']
    string_with_values = ''
    for num, value in enumerate(main_values):
        one_string = f"{num+1}. {value[0]} - {value[1]}\n"
        string_with_values += one_string
    return string_with_values
