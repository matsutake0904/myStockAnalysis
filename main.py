import requests
from send_img import send_message
import datetime
import pytz
import pandas as pd
import pandas_datareader as web

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://finance.yahoo.co.jp/quote/6502.T/history"
    pd.read_html(url)

    # time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    # time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    # send_message('send at ' + time_str)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
