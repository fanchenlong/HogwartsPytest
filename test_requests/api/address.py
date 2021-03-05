import requests

from test_requests.api.base import Base


class Address(Base):
    # def __init__(self):
        # self.s = None
        # super().__init__()
        #

        # url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2a5c74367a588b38&corpsecret=MoMQvfilqsl6QsOz6BsTIZpghLpDkbIfhfqFYRuhRow"
        # r = self.send("get",url)
        # #r = requests.get(url)
        # self.token = r['access_token']

    def add_member(self,userid:str,name:str,mobile:str,department:list,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        body.update(kwargs)
        return self.send("post",url, json=body)


    ##查找
    def get_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get",url)



###更新
    def update_meember(self,userid:str,name:str,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name}
        body.update(kwargs)
        return self.send("post",url, json=body)

##删除
    def delete_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get",url)

        #print(r.json())

f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid=kenan0012345"