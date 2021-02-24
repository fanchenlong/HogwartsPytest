import requests

import json

class TestDemo:

    ##获取token
    def setup(self):
        url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2a5c74367a588b38&corpsecret=MoMQvfilqsl6QsOz6BsTIZpghLpDkbIfhfqFYRuhRow"
        r = requests.get(url)
        ####self.token = r.json()['access_token']
        ###return self.token

        #print(self.token)
        errmsg = r.json()['errmsg']
        if errmsg == "ok":
            self.token = r.json()['access_token']
            print("token获取成功")
            return self.token
        else:
            print("token获取失败:",errmsg)

    ##增加，创建成员
    def test_post_created_personnel(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        body = {
            "userid": "mingren123",
            "name": "鸣人123",
            "mobile": "+86 13300000123",
            "department": [1],
        }
        r = requests.post(url,json=body)
        errmsg = r.json()['errmsg']
        if errmsg == "created":
            print("创建成员成功",r.json())
        else:
            print("创建成员失败：",errmsg)

    ##删除成员
    def test_get_delete_personnel(self):
        USERID = "mingren123"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={USERID}"
        r = requests.get(url)
        errmsg = r.json()['errmsg']
        if errmsg == "deleted":
            print("删除成员成功：",r.json())
        else:
            print("删除成员失败：", errmsg)

    ##更改成员信息
    def test_post_updated_personnel(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        body = {
            "userid": "mingren123",
            "name": "旋涡鸣人123"
        }
        r = requests.post(url,json=body)
        errmsg = r.json()['errmsg']
        if errmsg == "updated":
            print("更新成员信息成功",r.json())
        else:
            print("更新成员信息失败：",errmsg)

    ##查询成员信息
    def test_get_query_personnel(self):
        USERID = "mingren123"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={USERID}"
        r = requests.get(url)
        errmsg = r.json()['errmsg']
        if errmsg == "ok":
            print("查询成员成功",r.json())
        else:
            print("查询成员失败:",errmsg)
