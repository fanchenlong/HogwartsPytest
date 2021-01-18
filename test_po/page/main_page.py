###  企业微信主页  ###
from selenium.webdriver.common.by import By

from test_po.page.add_member_page import AddMemberPage
from selenium import webdriver

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage
from test_po.page.registered_page import RegisteredPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        print("sss")
        return ContactPage(self.driver)


    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        # driver = webdriver.Chrome()
        # driver.find_element(By.CSS_SELECTOR, "ww_indexImg_AddMember").click()
        #快捷键导入 alt+回车可以快捷导入
        return AddMemberPage(self.driver)
    #跳转到注册页面
    def goto_registered(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisteredPage