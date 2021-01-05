import json
from time import sleep


from selenium.webdriver.common.by import By
from selenium import webdriver

class TestTestbaidu():

    def setup_method(self):

############################### 用当前已经登录的浏览器打开 ############################
        ##用当前已经登录的浏览器打开
        chrome_args = webdriver.ChromeOptions()
       # chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        #self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

#####################################################################################

########################### 读取cookie并打开企业微信放在setup_method里 ###################
        # # 使用cookie登录前要知道在哪个页面登录的
        # self.driver.get("https://work.weixin.qq.com/")
        # # 以文件流的形式打开一个叫cookie.json给他r读的权限
        # with open("cookie.json", "r") as f:
        #     # 读取cookie，并把内容赋值给cookie
        #     cookies = json.load(f)
        # # 在网页注入cookie
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        #     # 打开企业微信地址
        #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #     sleep(3)
###################################################################


    def teardown_method(self):
        # pass
        # 关掉应用程序里打开的Chromedriver
        self.driver.quit()

    def test_cookie(self):

                #pass
################################ 这段是获取cookie的 ############
        # #获取cookie
        # cookie = self.driver.get_cookies()
        # #以文件流的形式打开一个叫cookie.json给他w写的权限
        # with open("cookie.json","w") as f:
        #     #吧获取到的cookie存储到cookie.json里
        #     ######print(cookie)
        #     json.dump(cookie,f)
#############################################################

############################# 这段是读取cookie的 ##############################
        #使用cookie登录前要知道在哪个页面登录的
        self.driver.get("https://work.weixin.qq.com/")
        #以文件流的形式打开一个叫cookie.json给他r读的权限
        with open("cookie.json","r") as f:
            #读取cookie，并把内容赋值给cookie
            cookies = json.load(f)
        #在网页注入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            #打开企业微信地址
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
###################################################################################
            # #点击 客户联系
        self.driver.find_element(By.XPATH, '// *[ @ id = "menu_customer"] / span').click()

            # 等待5秒
        sleep(5)
            # 关闭浏览器
        self.driver.close()
        print("点击【客户联系】成功")

    def test_qiyeweixn(self):
        pass
        # # #点击 客户联系
        # self.driver.find_element(By.XPATH, "//*[@class='frame_nav_item_title']").click()
        # # 等待5秒
        # sleep(5)
        # #关闭浏览器
        # self.driver.close()
        # print("点击【客户联系】成功")

