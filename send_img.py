import requests

TOKEN = 'VGaTitDsPy8mKYsRpDq5JxM5XgpwClTjhHWenD9gyRs'
api_url = 'https://notify-api.line.me/api/notify'
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}

def send_message(send_content):

    Send_dic = {'message': send_content}
    print(TOKEN_dic, ' ', Send_dic)
    requests.post(api_url, headers=TOKEN_dic, data=Send_dic)

def send_img(image_file):
    binary = open(image_file, mode='rb')

    image_dic = {'imageFile': binary}

    requests.post(api_url, headers=TOKEN_dic, data=image_dic)