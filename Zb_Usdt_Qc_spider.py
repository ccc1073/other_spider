import time
import requests
import json

from pymongo import MongoClient


class Zb_usdtqc(object):

    def __init__(self):

        self.api_url = 'https://trans.zb.cn/markets/klineLastData'

        self.data = {
            'needTickers': '1',
            'symbol': 'usdtqc',
            'type': '1day',
            'size': '1000',
        }

        # Mongo数据库客户端
        self.client = MongoClient('0.0.0.0', 0)
        self.collection = self.client["BOOMHASH"]["zb_udt_qc"]

    # 爬取与清洗
    def spiders(self):

        data_list = []

        reponse = requests.post(url=self.api_url, data=self.data)
        data = json.loads(reponse.content.decode())

        for i in data['datas']['data']:
            a = dict()
            a['Time'] = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(int(str(i[0])[0:-3])))
            a['Open'] = str(i[1])
            a['High'] = str(i[2])
            a['Low'] = str(i[3])
            a['End'] = str(i[4])
            a['VOLUME'] = str(i[5])

            data_list.append(a)

        return data_list


    # 写入mongodb
    def write_mongo(self, data_list):

        self.collection.collection.insert(data_list)

    # 开始爬起
    def start(self):

        data_list = self.spiders()
        self.write_mongo(data_list)


if __name__ == '__main__':
    zb = Zb_usdtqc()
    zb.start()