import pytest

from pythoncode.calculator import Calculator

import yaml

def get_datas():
    with open("./cal.yml") as f:
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
        return [add_datas,add_ids,sub_datas,sub_ids,mul_datas,mul_ids,div_datas,div_ids]


class TestCalc:


    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("\n计算开始")
    def teardown_method(self):
        print("\n计算结束")
####加法add
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        print(result)
        assert result == expect
####减法sub
    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[3])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        print(result)
        assert result == expect
####乘法mul
    @pytest.mark.parametrize("a,b,expect", get_datas()[4], ids=get_datas()[5])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        print(result)
        assert result == expect
####除法div
    @pytest.mark.parametrize("a,b,expect", get_datas()[6], ids=get_datas()[7])
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        print(result)
        assert result == expect
#


