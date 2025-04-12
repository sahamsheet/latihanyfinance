import yfinance as yf

def get_pe_pbv(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    if not info:
        print(f"Tidak dapat mengambil data untuk {ticker}.")
        return {'Ticker': ticker, 'PE Ratio': None, 'PBV': None}
    pe_ratio = info.get('trailingPE')
    pbv = info.get('priceToBook')
    return {'Ticker': ticker, 'PE Ratio': pe_ratio, 'PBV': pbv}

if __name__ == "__main__":
    adro_data = get_pe_pbv('ADRO.JK')
    ptba_data = get_pe_pbv('PTBA.JK')

    print("ADRO:")
    print(adro_data)
    print("\nPTBA:")
    print(ptba_data)
