###装饰器，用来点击元素时弹出了黑名单或弹窗，遍历黑名单或弹窗的后再运行的
import yaml
from selenium.webdriver.common.by import By


def handle_black(fun):
    def run(*args, **kwargs):
        #self是第0个参数需要传进来
        sinstance = args[0]
        with open("../black_list.yaml","r",encoding="utf-8") as f:
        ###黑名单或弹窗列表
            black_list = yaml.load(f)
        ###捕获异常（元素没找到）
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            #如果没找到相应的元素，就去黑名单链表找（遍历黑名单）
            for black in black_list:
                #如果发现黑名单的元素存在
                eles = sinstance.driver.find_elements(*black)
                ##就对黑名单元素进行处理
                if len(eles) > 0:
                    #通过点击的方式，关闭弹窗
                    eles[0].click()
                    #处理完就再次查找
                    return fun(*args, **kwargs)
            #没找到就报错
            raise e
    return run
