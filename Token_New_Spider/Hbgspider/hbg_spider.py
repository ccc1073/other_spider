import datetime
import time

from api.USDT_CNY_Trade_info import Get_Trade_info
from SunMongo import SunMongodb
from pymongo import MongoClient
from retry import retry

class Hbg_spider(object):
    def __init__(self):
        self.RunTime = 2
        self.collection = MongoClient('0.0.0.0', 00000)["BOOMHASH"]["USDT_CNY_NEW"]
        # self.collection = MongoClient('119.28.87.206', 21707)["BOOMHASH"]["USDT_CNY_NEW"]



    def run(self):
        global switch
        switch = 0

        while True:

            times = datetime.datetime.now().strftime('%M')

            if int(times) % self.RunTime == 0 and switch == 0:
                while True:
                    data = Get_Trade_info.Weighted_Mean()
                    if data['code'] ==200:
                        data_s =(float(data['price']))
                        time_s = int(time.time())
                        print(SunMongodb.insert_mongo(self.collection, dict(time=time_s,value=data_s)))
                        switch = 1
                        break


            if not int(times) % self.RunTime == 0:
                switch = 0

            time.sleep(2)

if __name__ == '__main__':
    Hbg_spider = Hbg_spider()
    Hbg_spider.run()