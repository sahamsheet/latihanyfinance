import yfinance as yf
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Konfigurasi Google Sheets API
try:
    with open('CREDSSHEET') as f:
        credentials_data = json.load(f)

    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_data, ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)
except FileNotFoundError:
    print("File credentials.json tidak ditemukan.")
    exit(1)
except Exception as e:
    print(f"Terjadi kesalahan saat memuat kredensial: {e}")
    exit(1)

# Buka Google Sheet
try:
    sheet = client.open('yfinanceauto').sheet1 # Ganti dengan nama Google Sheet Anda
except gspread.SpreadsheetNotFound:
    print("Google Sheet tidak ditemukan.")
    exit(1)
except Exception as e:
    print(f"Terjadi kesalahan saat membuka Google Sheet: {e}")
    exit(1)

# Daftar saham
saham = ['ADRO.JK', 'ITMG.JK', 'PTBA.JK']

# Ambil data PER dan PBV
data = [['Saham', 'PER', 'PBV']]
for ticker in saham:
    try:
        saham_info = yf.Ticker(ticker)
        info = saham_info.info
        per = info.get('trailingPE', 'N/A')
        pbv = info.get('priceToBook', 'N/A')
        data.append([ticker, per, pbv])
    except Exception as e:
        print(f"Gagal mengambil data untuk {ticker}: {e}")
        data.append([ticker, 'N/A', 'N/A'])

# Tulis data ke Google Sheet
try:
    sheet.clear()
    sheet.append_rows(data)
    print('Data PER dan PBV telah diunduh ke Google Sheet.')
except Exception as e:
    print(f"Terjadi kesalahan saat menulis data ke Google Sheet: {e}")
