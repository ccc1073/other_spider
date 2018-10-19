import datetime
import time
import pytesseract
import os

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Tradingview_spider(object):

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('~/Desktop/BOOMHASHS/tradingview_spider/chromedriver',chrome_options=chrome_options)
        # self.driver = webdriver.Chrome('/home/sunzhe/Python_Object/BOOMHASHS/tradingview_spider/chromedriver')
        self.open_chrome()

    def open_chrome(self):
        self.driver.get("https://cn.tradingview.com/symbols/USDTUSD")

    def get_png(self):
        times = int(time.time())
        self.driver.save_screenshot("{}.png".format(times))
        return str(times)

    def InitImage(self,name):
        images = Image.open('{}.png'.format(name))
        region = (0, 320, 170, 350)
        cropImg = images.crop(region)
        # os.remove('{}.png'.format(name))
        return pytesseract.image_to_string(cropImg, lang='chi_sim')


    def start(self):
        switch = 0
        while True:
            times = datetime.datetime.now().strftime('%M')
            # if int(times) % 5 == 0 and switch == 0:
            if True:

                png_name = self.get_png()
                data = self.InitImage(png_name)
                print('时间戳:{},数据:{}'.format(png_name,data))
                switch = 1

            else:
                print('等待中...')
                switch = 0


if __name__ == '__main__':
    sp = Tradingview_spider()
    a = sp.start()