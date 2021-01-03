import pytest
# fixture是 pytest的一个外壳函数，可以模拟setu和teardown的操作
# yield之前的操作相当于setup，yield之后的操作相当于teardown
# yield 想打哪国语return，如果返回数据的话，直接放在yield的后面


# 创建一个登陆的fixture方法
#在括号里加 autouse=True就可以全部都执行，True是打开,但是拿不到返回值，如果想拿到返回值需要吧这个方法传入test_case1(login)
@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    username = "tom"
    password = "123456"
    token = "token123456"
    #把参数放到yield里
    yield [username,password,token]
    print("登出操作")

#测试用例1：需要提前登陆
def test_case1():
    #获取yield中的参数
    print(f"login username and password:{login}")
    print("测试用例1")

#测试用例2：不需要提前登陆
def test_case2(connectDB):
    print("测试用例2")

#测试用例1：需要提前登陆
def test_case3():
    print("测试用例3")


#测试用例1：需要提前登陆
#@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")