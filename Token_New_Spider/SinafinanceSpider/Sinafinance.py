#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Author Sunnnn
import time

import requests
import re

class Sinafinance(object):

    @staticmethod
    def getPrice(token_code):

        """
        获得货币对当前汇率
        token_name > 货币对
        demo > https://hq.sinajs.cn/list=fx_s[usdcny] 注:[]标示中的内容对应token_name
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Host': 'hq.sinajs.cn'
                }
        try:

            response = requests.get('https://hq.sinajs.cn/list=fx_s{}'.format(token_code), headers=headers)
            response_content = response.content.decode('GBK')
            data = re.findall(',(.*?),美元兑人',response_content)
            data = float(data[0].split(',')[-1])
            return dict(code=200,price=data)

        except:

            return dict(code=500, price=0)



if __name__ == '__main__':
    with open('1.txt','a+') as f:

        while True:
            tether = Sinafinance.getPrice('usdcny')
            data = str(tether)  + '  --------  ' + str(int(time.time())) + '\n'
            print(data)
            f.write(data)
            time.sleep(1)
