#注册页面
from selenium.webdriver.common.by import By
from test_po.page.base_page import BasePage




class RegisteredPage(BasePage):
    def Registered(self):
        self.find(By.ID, "corp_name").send_keys("test1313")
        self.find(By.ID, "corp_name").send_keys("test1313")