#封装基本的方法
import os

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

#封装一个读取yaml的方法
def get_data():
    # ## 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    # path1 = os.path.abspath(__file__)
    # print(path1)
    # ## 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    # path2 = os.path.dirname(path1)
    # print(path2)
    # ## 3、dirname 可以获取当前路径上一级目录所在的绝对路径--A文件夹的绝对路径
    # path3 = os.path.dirname(path2)
    # print(path3)
    # ## 综上先获取文件的绝对路径，再使用两层的 dirname 就可以获取到根目录的绝对路径
    # ## 结合来写：获得根目录绝对路径
    # A_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(A_DIR)
    ########摘抄自https: // www.cnblogs.com / shouhu / p / 12149553.html
                    #通过os获取yaml的路径
    yaml_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/data.yaml"

    with open(yaml_file_path, encoding='utf-8') as f:
        # with open('../data/data.yaml', encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data

class Basepage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver
    #封装find_element方法
    def find(self,locator):
        return self.driver.find_element(*locator)
    #点击的方法
    def find_and_click(self,locator):
        self.find(locator).click()
    #输入的方法
    def find_and_send_keys(self,locator,text):
        self.find(locator).send_keys(text)
    #滑动查找并点击的方法
    def scorll_find_click(self,text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().' 
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)
    def find_and_get_test(self,locator):
        return self.find(locator).text



