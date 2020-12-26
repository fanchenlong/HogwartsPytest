import pytest

def setup_module():
    print("\nsetup_module:整个test_setup_teardown.py模块 开始前执行一次")
def teardown_module():
    print("\nsetup_module:整个test_setup_teardown.py模块结束前执行一次")


def setup_function():
    print("\nsetup_function不在类中的用例前执行")
def teardown_function():
    print("\nteardown_function不在类中的用例后执行")
def test_three():
    print("正在执行test_three")

def test_four():
    print("正在执行test_four")

class TestClass():

    def setup_class(self):
        print("\nnsetup_class:所有用例执行前")
    def teardown_class(self):
        print("\nteardown_class:所有用例结束后执行")

    def setup_method(self):
        print("\nsetup_method:每个用例开始前执行")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束后执行")

    def test_one(self):
        print("正在执行test_one")
    def test_teo(self):
        print("正在执行test_two")