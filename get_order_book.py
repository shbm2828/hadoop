import pandas as pd
from SmartApi import SmartConnect
from pyotp import TOTP
import os
import urllib
import json


#counter_1min = 105

TOTP("").now()
key_path = r"D:\key"
os.chdir(key_path)
key_secret = open("shbm_key.txt", "r").read().split()
obj = SmartConnect(api_key=key_secret[0])
data = obj.generateSession(key_secret[2],key_secret[3], TOTP(key_secret[4]).now())

instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())


def get_order_book():
    response = obj.orderBook()   #response is a dict type
    print(response["data"])
    #print(response["data"])
    #orderdf = pd.DataFrame(response['data'])
    
get_order_book()
