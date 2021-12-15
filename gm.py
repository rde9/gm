# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/3 19:18
@Auth ： d1rrick@scientistDAO
@File ：autochat.py
@IDE ：PyCharm

@Modified_by : rh9yep@scientistDAO
@Modified_time : 2021/12/15 21:08
"""
import requests
import json
import random
import time
import traceback

channel_list = []
authorization_list = []

def chat():
    for authorization in authorization_list: # accounts
        header = {
            "Authorization":authorization,
            "Content-Type":"application/json",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        for channel_id in channel_list: # channels
            msg = {
                "content": 'gm',
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False
            }
            url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.content)
                time.sleep(random.randrange(10,15))
            except:
                print(traceback.format_exc())
                break
        time.sleep(random.randrange(30,50))



if __name__ == '__main__':
    while True:
        try:
            chat()
            sleeptime = random.randrange(64800, 86400) # sleep 18-24 hours
            time.sleep(sleeptime)
        except:
            print(traceback.format_exc())
            break
