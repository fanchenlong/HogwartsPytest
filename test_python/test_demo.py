# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    print("这是我的第一条测试用例")
    assert inc(3) == 4
def test_foo():
    print("这是我的第二条测试用例")
    assert inc(3) == 4
