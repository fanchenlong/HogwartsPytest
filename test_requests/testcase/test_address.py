import pytest

from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
    @pytest.mark.parametrize("userid,mobile",[("lisi00128","13261998888"),
                                              ("lisi00129","13261998889"),
                                              ("lisi00120","13261998890")])
    def test_add_member(self,userid,mobile):
        name = "今天是星期六_27"
        department = [1]
        # 数据清理
        self.address.delete_member(userid)
        # 创建成员
        self.address.add_member(userid=userid,name=name,mobile=mobile,department=department)
        # 查询结果
        r = self.address.get_member(userid)
        assert r.get('name',"userid添加失败") == name

