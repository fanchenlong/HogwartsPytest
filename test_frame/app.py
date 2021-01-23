###对app的操作
#启动app、关闭app、重启app、进入首页.........
from appium import webdriver

from test_frame.basepage import BasePage
from test_frame.page.main_page import MainPage





class App(BasePage):
    #启动app
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["deviceName"] = "wework"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            # 设置页面等待空闲状态的时间为1秒
            caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
           ##隐试等待10S
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self
    #重启app
    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self
    #停止App
    def stop(self):
        self.driver.quit()
        return self
    #进入首页
    def goto_main(self)->MainPage:
        #跳转首页
        return MainPage(self.driver)