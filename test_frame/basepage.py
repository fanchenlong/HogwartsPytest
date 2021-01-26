#封装基本的方法
import os

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

#封装一个读取yaml的方法
from test_frame.handle_black import handle_black


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
    yaml_file_path = os.path.abspath(__file__) + "black_list.yaml"

    with open(yaml_file_path, encoding='utf-8') as f:
        # with open('../data/data.yaml', encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data

class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver
    #封装find_element方法
    @handle_black
    def find(self,locator):
        return self.driver.find_element(*locator)
       # ###黑名单或弹窗列表
       #  black_list = [(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]
       # ###捕获异常（元素没找到）
       #  try:
       #      #若果找到相应的元素直接点击返回
       #     result = self.driver.find_element(*locator)
       #     return result
       #  except Exception as e:
       #      #如果没找到相应的元素，就去黑名单链表找（遍历黑名单）
       #      for black in black_list:
       #          #如果发现黑名单的元素存在
       #          eles = self.driver.find_elements(*black)
       #          ##就对黑名单元素进行处理
       #          if len(eles) > 0:
       #              #通过点击的方式，关闭弹窗
       #              eles[0].click()
       #              #处理完就再次查找
       #              return self.find(locator)
       #      #没找到就报错
       #      raise e
       #



    #点击的方法
    def find_and_click(self,locator):
        self.find(locator).click()
    #输入的方法
    def find_and_send_keys(self,locator,text):
        self.find(locator).send_keys(text)

    def send(self,locator,content):
        self.find(locator).send_keys(content)
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

    def run_steps(self,page_path,operation):
        #yamll 的读取
        with open(page_path,'r',encoding="utf-8") as f:
            data = yaml.load(f)
        #支持 PO下多个操作
        steps = data[operation]
        #遍历每一个动作
        for step in steps:
            action = step['action']
            #如果动作是find_and_click，就调用basepage中的find_and_click
            if action == "find_and_click":
                # 调用find_and_click传入相应参数
                self.find_and_click(step['locator'])
            elif action == "send":
                self.send(step['locator'],step['content'])



