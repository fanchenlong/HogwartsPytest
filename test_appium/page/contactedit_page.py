###手动添加编辑成员信息页面


#编辑成员信息
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.basepage import Basepage


class ContactEditPage(Basepage):
    # def __init__(self,driver):
    #     self.driver = driver
    #编辑姓名
    def edit_name(self,name):
        ##姓名
        self.driver.find_element(
            MobileBy.XPATH,
            "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self
    #性别
    def edit_gender(self,gender):
        #判断男这个可不可以点击等待10秒内可点击的时候进行点击
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver,10).until(
            expected_conditions.element_to_be_clickable(locator))
        ele.click()
        ##性别
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 判断点击男女
        if gender == '女':
            #self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            #self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        return self
    #手机号
    def edit_phonenum(self,phonenum):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").\
            send_keys(phonenum)
        return self
    #点击保存
    def click_save(self):
        #局部导入
        from test_appium.page.memberinbite_page import MemberInbitePage
        #点击保存操作
        #self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/gur"))
        return MemberInbitePage(self.driver)