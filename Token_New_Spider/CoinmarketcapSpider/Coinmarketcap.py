#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Author Sunnnn

import requests
from lxml import etree


class Coinmarketcap(object):

    @staticmethod
    def getPrice(token_code):

        """
        获得货币当前价格
        token_name > 货币名称
        demo > https://Coinmarketcap.com/currencies/[tether]/ 注:[]标示中的内容对应token_name
        """
        try:
            response = requests.get('https://coinmarketcap.com/currencies/{}/'.format(token_code))
            response_content = response.content.decode()
            html_code = etree.HTML(response_content)
            toekn_data = html_code.xpath('//*[@id="quote_price"]/span[1]')
            return dict(code=200,price=toekn_data[0].text)

        except:
            return dict(code=500, price=0)



if __name__ == '__main__':
    tether = CoinmarketcapSpider.getPrice('tether')
    print(tether)
