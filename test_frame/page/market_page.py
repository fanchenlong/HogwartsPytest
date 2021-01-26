##行情页面
import yaml
from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
        #点击搜索方法
    def goto_search(self):
        self.run_steps("../page/market_page.yaml","goto_search")
        # #yamll 的读取
        # with open("../page/market_page.yaml",'r',encoding="utf-8") as f:
        #     data = yaml.load(f)
        # #遍历每一个动作
        # for step in data:
        #     action = step['action']
        #     #如果动作是find_and_click，就调用basepage中的find_and_click
        #     if action == "find_and_click":
        #         # 调用find_and_click传入相应参数
        #         self.find_and_click(step['locator'])
        #点击搜索操作
        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)