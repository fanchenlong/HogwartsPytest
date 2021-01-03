# -*- coding: utf-8 -*-
import pytest

#module,session(一次执行多个py但是这个只在开头结尾使用一次)
import yaml


import os

from test_python.pythoncode.calculator import Calculator


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算机实例")
    calc = Calculator()
    return calc
#####################################
#通过os.path.dirnam获取当前文件所在路径
yaml_file_path = os.path.dirname(__file__) + "/cal.yml"

with open(yaml_file_path,encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    print(datas)
    ##加
    add_datas = datas["add_datas"]
    add_ids = datas["add_ids"]
    ##减
    sub_datas = datas["sub_datas"]
    sub_ids = datas["sub_ids"]
    ##乘
    mul_datas = datas["mul_datas"]
    mul_ids = datas["mul_ids"]
    ##除
    div_datas = datas["div_datas"]
    div_ids = datas["div_ids"]
###加
@pytest.fixture(params=add_datas,ids=add_ids)
def add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param是：{data}")
    yield data
    print("结束计算")
####减
@pytest.fixture(params=sub_datas,ids=sub_ids)
def sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param是：{data}")
    yield data
    print("结束计算")
###乘
@pytest.fixture(params=mul_datas,ids=mul_ids)
def mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param是：{data}")
    yield data
    print("结束计算")
###除
@pytest.fixture(params=div_datas,ids=div_ids)
def div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param是：{data}")
    yield data
    print("结束计算")
