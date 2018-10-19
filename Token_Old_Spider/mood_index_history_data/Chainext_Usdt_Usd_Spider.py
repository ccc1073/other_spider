import json

import requests
from SunMongo import SunMongodb
from pymongo import MongoClient
from threading import Thread

def async_call(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper

class Zb_Usdt_Qc_spider(object):

    def __init__(self, start_api):

        # MODO索引历史数据 接口
        self.mood_index_history_data_api_url = 'https://api.chainext.io/v1/mood_index_history_data?id=90001'

        # 历史数据 接口
        self.ls_api_url = 'https://api.chainext.io/v1/mood_history?id=90001'

        # USDT/CNY价格 接口
        self.USDT_CNY_api_url = 'https://api.chainext.io/v1/cny_price?id=90001'

        # USD/CNY价格 接口
        self.USD_CNY_api_url = 'https://api.chainext.io/v1/cny_price?id=90001&type=usd'

        api_dict = {
            'ls_api_url' : self.ls_api_url,
            'USDT_CNY_api_url' : self.USDT_CNY_api_url,
            'USD_CNY_api_url' : self.USD_CNY_api_url,
            'mood_index_history_data_api_url' : self.mood_index_history_data_api_url,
        }

        # 选择接口
        self.start_api = api_dict[start_api]

        # Mongo数据库客户端
        self.client = MongoClient('0.0.0.0', 00000)
        self.collection = self.client["BOOMHASH"]["USDT_USD_OLD"]

    def get_response(self):
        reponse = requests.get(self.start_api)
        reponse = json.loads(reponse.content.decode())
        return reponse

    # 开启爬虫
    def start(self):
        response_dicet = self.get_response()
        num = 0
        for i in response_dicet['data']:
            data = dict(
                time=str(i[0])[0:-2],
                value=str(i[1])
            )
            num += 1
            SunMongodb.insert_mongo(self.collection, data)
            print('正在处理{}, 现在已经是第{}条'.format(str(data),num))


if __name__ == '__main__':
    a = Zb_Usdt_Qc_spider('mood_index_history_data_api_url')
    a.start()
