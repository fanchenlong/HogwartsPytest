import pytest

from pythoncode.calculator import Calculator
import getyam_open_cal


##################  想把读取yam的方法单独封装，还没成功引用
class TestCalc:
    get_datas = getyam_open_cal.get_datas()
    def setup_class(self):
        self.calc = Calculator()



    def setup_method(self):
        print("\n计算开始")

    def teardown_method(self):
        print("\n计算结束")

    ####加法add
    @pytest.mark.parametrize("a,b,expect", get_datas[0], ids=get_datas[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        print(result)
        assert result == expect

    ####减法sub
    @pytest.mark.parametrize("a,b,expect", get_datas[2], ids=get_datas[3])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        print(result)
        assert result == expect

    ####乘法mul
    @pytest.mark.parametrize("a,b,expect", get_datas[4], ids=get_datas[5])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        print(result)
        assert result == expect

    ####除法div
    @pytest.mark.parametrize("a,b,expect", get_datas[6], ids=get_datas[7])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        print(result)
        assert result == expect
#
