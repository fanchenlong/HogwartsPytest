###添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import Basepage
from test_appium.page.contactedit_page import ContactEditPage


class MemberInbitePage(Basepage):
    # def __init__(self,driver):
    #     self.driver = driver
    # 点击手动添加
    def addconect_menual(self):
        #点击手动输入添加的操作
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        #跳转到手动添加编辑成员信息页面
        return ContactEditPage(self.driver)

    #获取toast
    def get_toast(self):
        # ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        ele = self.find_and_get_test((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        return ele
