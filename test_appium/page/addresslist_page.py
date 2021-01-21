###通讯录页面
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import Basepage
from test_appium.page.memberinbite_page import MemberInbitePage


class AddresslistPage(Basepage):
    # def __init__(self,driver):
    #     self.driver = driver
    # 点击添加成员
    def add_member(self):
        ###如果人多需要滑动查找添加成员按钮
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.scorll_find_click("添加成员")
        #跳转到添加成员页面
        return MemberInbitePage(self.driver)