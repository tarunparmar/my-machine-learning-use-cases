"""
Fetch the daily stock prices using python_datareader from MorningStar for stocks in S&P500.
@author: tarunparmar
"""

# Company list reference
# https://stackoverflow.com/questions/25338608/download-all-stock-symbol-list-of-a-market

import os
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import urllib.request

BASE_DIR = os.getcwd()+'/data'
SP500_LIST_URL = "https://datahub.io/core/s-and-p-500-companies/r/constituents.csv"
SP500_LIST_PATH = os.path.join(DATA_DIR, "constituents.csv")

def _download_sp500_list():
    if os.path.exists(SP500_LIST_PATH):
        return

    f = urllib.request.urlopen(SP500_LIST_URL)
    print("Downloading ...", SP500_LIST_URL)
    with open(SP500_LIST_PATH, 'w') as fin:
        print(fin, f.read())
    return

def _load_symbols():
    _download_sp500_list()
    df_sp500 = pd.read_csv(SP500_LIST_PATH)
    # df_sp500.sort_values('Market Cap', ascending=False, inplace=True)
    stock_symbols = df_sp500['Symbol'].unique().tolist()
    print("Loaded %d stock symbols" % len(stock_symbols))
    return stock_symbols

