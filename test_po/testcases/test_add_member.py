###  添加成员用例
from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        # 实例化mainpage类
        self.main = MainPage()
    def test_add_member(self):

        #1.首页跳转到添加成员页面  2.添加成员   3.获取成员信息
        result = self.main.goto_add_member().add_member().get_list()
        assert "刀锋" in result

    def test_add_department(self):
        #1.首页跳转到通讯录页面  2.添加部门   3.获取部门信息
        result = self.main.goto_contact().add_department()
        assert "测试" in result