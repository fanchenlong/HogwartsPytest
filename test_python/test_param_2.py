import pytest

#参数可以组合堆叠使用

@pytest.mark.parametrize("a",[0,1,3])
@pytest.mark.parametrize("b",[2,3,6])
def test_foo(a,b):
    print("测试参数堆叠组合:a->%s,b->%s"%(a,b))