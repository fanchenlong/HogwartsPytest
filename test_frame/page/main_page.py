##雪球的main，首页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    #跳转到行情的方法
    def goto_market_page(self):
        ###模拟此时在点击行情前面出现黑名单或弹窗
        self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))

        #点击行情测操作
        self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
