#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Author Sunnnn

import datetime
import time

from Coinmarketcap import Coinmarketcap
from SunMongo import SunMongodb
from pymongo import MongoClient



class CoinmarketcapSpider(object):
    def __init__(self):
        self.RunTime = 2
        self.collection = MongoClient('0.0.0.0', 0)["BOOMHASH"]["USDT_USD_NEW"]

    def run(self):

        global switch
        switch = 0

        while True:

            times = datetime.datetime.now().strftime('%M')

            if int(times) % self.RunTime == 0 and switch == 0:
                while True:
                    data = Coinmarketcap.getPrice('tether')
                    if data['code'] ==200:
                        data_s =(float(data['price'])*100)
                        time_s = int(time.time())
                        print(SunMongodb.insert_mongo(self.collection, dict(time=time_s,value=data_s)))
                        switch = 1
                        break


            if not int(times) % self.RunTime == 0:
                switch = 0

            time.sleep(2)

if __name__ == '__main__':
    CoinmarketcapSpider = CoinmarketcapSpider()
    CoinmarketcapSpider.run()