import requests
from send_img import send_message
import datetime
import pytz
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    send_message('send at ' + time_str)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
