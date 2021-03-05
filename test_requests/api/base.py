import requests


class Base:
    def __init__(self):
        url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2a5c74367a588b38&corpsecret=MoMQvfilqsl6QsOz6BsTIZpghLpDkbIfhfqFYRuhRow"
        r = requests.get(url).json()
        self.token = r['access_token']
        #声明一个Session
        self.requests_session = requests.Session()
        #把token放入到Session中
        self.requests_session.params = {'access_token':self.token}

    def send(self,*args,**kwargs):
        #用Session
         r = self.requests_session.request(*args,**kwargs)
         return r.json()