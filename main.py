import requests
import time
import os
from random import randint


def upload(photo_name):
    url = 'https://api.telegram.org/bot{0}/sendPhoto'.format(token)
    files = {'photo': open(photo_name, 'rb')}
    data = {'chat_id': chat_id}
    r = requests.post(url, files=files, data=data)
    print(r.json())
    os.remove(photo_name)
    del r


def select():
    path = os.listdir('.')
    num = randint(0, len(path))
    photo_name = path.pop(num)
    return photo_name


photo_path = input('Input path to photo: ')
token = input('Input bot token: ')
chat_id = input('Input chat id: ')
os.chdir(photo_path)

count = 0
while True:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    print('Number of post: {0}'.format(count))
    count += 1
    print('Starting uploading process...')
    upload(select())
    print('60 minutes to next post')
    time.sleep(900)
    print('45 minutes to next post')
    time.sleep(900)
    print('30 minutes to next post')
    time.sleep(900)
    print('15 minutes to next post')
    time.sleep(900)

