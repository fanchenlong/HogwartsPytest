###  通讯录页面   ###
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        pass

    def add_department(self):
        self.find(By.XPATH, '//*[@class="member_colLeft_top_addBtn"]').click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        self.find(By.CSS_SELECTOR, '[name=name]').send_keys("测试")
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850718792885_anchor']").click()
        self.find(By.CSS_SELECTOR, ".qui_btn ww_btn ww_btn_Blue").click()
        department_name = self.find(By.ID, "party_name").text
        return department_name(self.driver)


    def get_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """

        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)

        return name_list