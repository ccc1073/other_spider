# -*- coding: utf-8 -*-

import datetime
import time
import json
import requests

from jsonpath import jsonpath
from decimal import Decimal

class Get_Trade_info(object):

    heard = {
        'User-Agent': 'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,likeGecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)'
    }


    @staticmethod
    def Sell_Usdt():
        try:
            response = requests.get('https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=2&tradeType=sell&blockType=general&online=1', headers=Get_Trade_info.heard)
            response = json.loads(response.content.decode())
        except Exception:
            return 0

        number = Decimal(0.0)

        for i in response['data']:

            data = Decimal(jsonpath(i, '$..price')[0])
            number += data
        return number

    @staticmethod
    def Buy_Usdt():
        try:
            response = requests.get('https://otc-api.eiijo.cn/v1/data/trade-market?country=37&currency=1&payMethod=0&currPage=1&coinId=2&tradeType=buy&blockType=general&online=1', headers=Get_Trade_info.heard)

            response = json.loads(response.content.decode())

        except Exception:
            return 0

        number = Decimal(0.0)

        for i in response['data']:

            data = Decimal(jsonpath(i, '$..price')[0])
            number += data
        return number

    # 输出加权平均后的结果
    @staticmethod
    def Weighted_Mean():
        try:
            times = int(time.time())
            while True:
                sell_data = Get_Trade_info.Sell_Usdt()
                time.sleep(2)
                buy_data = Get_Trade_info.Buy_Usdt()

                if not (int(sell_data) and int(buy_data)) ==0:
                    break

            result = sell_data + buy_data
            result = round(result/20, 2)
            return dict(code=200, price=float(result))
        except Exception as e:
            print(e)

            return dict(code=500, price=0)
if __name__ == '__main__':

    Get_Trade_info.Buy_Usdt()