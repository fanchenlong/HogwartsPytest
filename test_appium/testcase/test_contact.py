

import pytest
import yaml
from test_appium.page import basepage

from test_appium.page.app import App
##去取yaml文件
# def get_data():
#         with open('../data/data.yaml',encoding="UTF-8") as f:
#             data = yaml.safe_load(f)
#             add_data = data['add']
#             return add_data

class TestContact:
    #读取yaml的实例化
    get_data = basepage.get_data()
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()
   #参数化
    # @pytest.mark.parametrize("name,gender,phonenum",[
    #                          ["liliu1","男","18800000001"],
    #                          ["liliu2","女","18800000002"]])
    ##读取yaml参数化
    @pytest.mark.parametrize("name,gender,phonenum",get_data)
    def test_add_contact(self,name,gender,phonenum):
        # name = "zhangsi3"
        # gender = "男"
        # phonenum = '13400000003'
        toast = self.main.click_addresslist().add_member().addconect_menual().\
                edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast()
        assert toast == "添加成功"