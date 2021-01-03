import pytest
import yaml
# yaml参数化
def get_datas():
    with open("datayam.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        return [add_datas,add_ids]

def add_functuon(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",get_datas()[0],
                        ids=get_datas()[1])
def test_add(a,b,expected):
    assert add_functuon(a,b) == expected