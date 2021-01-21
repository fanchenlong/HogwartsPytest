# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #隐试等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/guu")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/fk1")
        el2.send_keys("电不信")
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/d2f")
        el3.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/dx1")
        el5.send_keys("123")
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dwx")
        el6.click()

    #打卡
    def test_daka(self):
        #点击工作台
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        #滑动点击打卡（因为当前不可见需要滑动）
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        #点击外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        #用包含定位 次外出 点击打卡
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        #打卡成功定位
        r = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/mn").text
        #断言打卡成功
        assert r == "外出打卡成功"

    #通讯录添加成员
    def test_tianjiachengyuan(self):
        name = "zhangsan1"
        gender = "女"
        phonenum = '13300000001'
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        #点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        #选择手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        ####以下手动输入页面
        ##姓名
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        ##性别
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        #判断点击男女
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        ##手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(phonenum)
        #保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        #保存成功tost定位
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert ele == "添加成功"