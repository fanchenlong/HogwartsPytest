###  添加成员页面 ###
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    #_username前面加下划线公有的变为私4有的
    _username = (By.ID, "username")
    def add_member(self):
        #输入成员信息点击保存
        #*self._username前 加*是解元组，相当于self.find(By.ID, "username")
        self.find(*self._username).send_keys("德邦总管")
        self.find(By.ID, "memberAdd_acctid").send_keys("13312345")
        self.find(By.ID, "memberAdd_phone").send_keys("13312345678")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member2(self):
        # 输入成员信息点击保存
        self.find(By.ID, "username").send_keys("德邦总管")
        self.find(By.ID, "memberAdd_acctid").send_keys("13312345")
        self.find(By.ID, "memberAdd_phone").send_keys("13312345678")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)