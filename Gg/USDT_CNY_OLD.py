import requests
import json
import time

from SunMongo import SunMongodb
from pymongo import MongoClient

response = requests.get('https://graphs2.coinmarketcap.com/currencies/tether/')
data = response.content.decode()
data = json.loads(data)
data = data['price_usd'][1030:1316]
num = 0
collection = MongoClient('0.0.0.0', 0)["BOOMHASH"]["USDT_USD_OLDS"]

for i in data:

    times = int(i[0]/1000)

    times = time.strftime("%Y--%m--%d 08:00:00", time.localtime(int(times)))

    timeArray = time.strptime(times, "%Y--%m--%d %H:%M:%S")
    tt = int(time.mktime(timeArray))
    value = i[1]
    print(SunMongodb.insert_mongo(collection, dict(time=tt, value=value)))
