import pytest
#scopede作用域不一样 值function，class（类前后），module（整个文件的前后）
#
# fixture 用法
# 定义
# @pytest.fixture()
# def fixture_method():
#     print("setup")
#     yield 返回值
#     print("teardown")
# 调用方法
# 测试用例中传入 fixture 方法名
# @pytest.mark.usefixtures(“login”)
# 自动调用 @pytest.fixture(autouse=True)
# 作用域
# 控制方式：@pytest.fixture(scope="")
# scope 的取值
# function （默认值）
# class
# module
# session
# fixture 方法返回值的获取
# 在测试用例中使用 fixture 方法名可以获取到 yield 后面的返回值
#
# conftest.py 用法
# conftest.py 文件名是不能改变
# conftest.py 与运行的用例要在同一个 package 下
# 不需要 import 导入 conftest.py，pytest 用例会自动查找
# 所有同目录测试文件运行前都会执行 conftest.py 文件
# 全局的配置和前期工作都可以写在这里


# @pytest.fixture(scope="module")
# def connectDB():
#     print("连接数据库操作")
#     yield
#     print("断开数据库连接")

class TestDemo:

    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")

class TestDemo2:

    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")