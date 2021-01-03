# -*- coding: utf-8 -*-
import pytest



# @pytest.fixture(scope="class")
# def get_calc():
#     print("获取计算机实例")
#     cala = Calculator
#     return cala
# import yaml

# with open("./cal.yml") as f:
#     datas = yaml.safe_load(f)
#     print(datas)
#     ##加
#     add_datas = datas["add_datas"]
#     add_ids = datas["add_ids"]
#     ##减
#     sub_datas = datas["sub_datas"]
#     sub_ids = datas["sub_ids"]
#     ##乘
#     mul_datas = datas["mul_datas"]
#     mul_ids = datas["mul_ids"]
#     ##除
#     div_datas = datas["div_datas"]
#     div_ids = datas["div_ids"]


# @pytest.fixture(params=add_datas, ids=add_ids)
# def get_datas(request):
#     print("开始计算")
#     data = request.param
#     print(f"request.param是：{data}")
#     yield data
#     print("结束计算")

class TestCalc:


####加法add
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,add_datas):
        result = None
        try:
            result = get_calc.add(add_datas[0],add_datas[1])
            #print(result)
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == add_datas[2]


######除法div
    @pytest.mark.run(order=4)
    def test_div(self,get_calc,div_datas):
        result = None
        try:
            result = get_calc.div(div_datas[0], div_datas[1])
    # print(result)
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == div_datas[2]

####减法sub
    @pytest.mark.run(order=2)
    def test_sub(self,get_calc,sub_datas):
        result = None
        try:
            result = get_calc.sub(sub_datas[0],sub_datas[1])
            #print(result)
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == sub_datas[2]

####乘法mul
    @pytest.mark.run(order=3)
    def test_mul(self,get_calc,mul_datas):
        result = None
        try:
            result = get_calc.mul(mul_datas[0],mul_datas[1])
            #print(result)
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == mul_datas[2]





#
