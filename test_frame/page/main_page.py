##雪球的main，首页
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    #跳转到行情的方法
    def goto_market_page(self):
        self.run_steps("../page/main_page.yaml","goto_market_page")
        # #yamll 的读取
        # with open("../page/main_page.yaml",'r',encoding="utf-8") as f:
        #     data = yaml.load(f)
        # #遍历每一个动作
        # for step in data:
        #     action = step['action']
        #     #如果动作是find_and_click，就调用basepage中的find_and_click
        #     if action == "find_and_click":
        #         # 调用find_and_click传入相应参数
        #         self.find_and_click(step['locator'])
        # ###模拟此时在点击行情前面出现黑名单或弹窗
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        #
        # #点击行情测操作
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)

    def goto_mine(self):
        self.run_steps("../page/main_page.yaml","goto_mine")

