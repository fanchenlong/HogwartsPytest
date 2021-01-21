###主页
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddresslistPage
from test_appium.page.basepage import Basepage


class MainPage(Basepage):
    # def __init__(self,driver):
    #     self.driver = driver
    # 点击通讯录
    def click_addresslist(self):
        # 点击通讯录操作
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        #跳转通讯录页面
        return AddresslistPage(self.driver)