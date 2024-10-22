import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

#Authenticate and connect to Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C://Users//kmitsios//Downloads//posttestproject-392811-67f665219ae7.json', scope)
client = gspread.authorize(creds)

#Open your Google Sheet by URL
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/146fpYNd0TAUVdsDqe1jo16zIahZm_Dk88XenxXDMGJw/edit?gid=0')
worksheet = spreadsheet.get_worksheet(0)  #first worksheet

next_row = len(worksheet.get_all_values()) + 1

#Prepare data
current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
id_value = next_row - 1
current_user = os.getlogin()
curse_word = "testword" #placeholder
whine_word = ""  #placeholder

#Append row
worksheet.append_row([id_value, current_timestamp, current_user, curse_word, whine_word])

print(f"Data appended successfully to row {next_row}!")
