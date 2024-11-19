import os
from common.http_client import HttpClient
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

#对用户模块相关的不需要控制访问的公共HTTP api请求进行简单封装为http_client
class IndexUserHttpClient(HttpClient):

    def __init__(self, api_root_url, **kwargs):
        super(IndexUserHttpClient, self).__init__(api_root_url+"/index", **kwargs)

    #获取公钥
    def get_publish_key(self, **kwargs):
        return self.get("/getPublicKey", **kwargs)

    #获取RSA公钥加密后的数据
    def get_rsa_ecode_password(self,**kwargs):
        return self.post(f"/getRsaEncodePassword" ,**kwargs)

    #注册用户
    def register(self,**kwargs):
        return self.post("/register",**kwargs)

    #用户登录
    def login(self,**kwargs):
        return self.post("/login", **kwargs)

    #用户登出
    def logout(self, **kwargs):
        return self.post("/logout",**kwargs)




index_user_http_client = IndexUserHttpClient(api_root_url)