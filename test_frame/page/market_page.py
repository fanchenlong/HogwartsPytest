##行情页面

from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
        #点击搜索方法
    def goto_search(self):
        #点击搜索操作
        self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)