import yfinance as yf
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Konfigurasi Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('CREDS', scope) #Ganti nama_file_kredensial_anda.json dengan nama file json anda.
client = gspread.authorize(creds)

# Buka Google Sheet
sheet = client.open('yfinanceauto').sheet1 #Ganti Nama Google Sheet anda dengan nama google sheet anda.

# Daftar saham
saham = ['ADRO.JK', 'ITMG.JK', 'PTBA.JK']

# Ambil data PER dan PBV
data = [['Saham', 'PER', 'PBV']]
for ticker in saham:
    saham_info = yf.Ticker(ticker)
    info = saham_info.info
    per = info.get('trailingPE', 'N/A')
    pbv = info.get('priceToBook', 'N/A')
    data.append([ticker, per, pbv])

# Tulis data ke Google Sheet
sheet.clear()
sheet.append_rows(data)

print('Data PER dan PBV telah diunduh ke Google Sheet.')
