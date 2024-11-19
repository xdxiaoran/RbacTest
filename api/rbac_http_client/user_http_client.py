import os
from common.http_client import HttpClient
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


#对用户模块相关的需要控制访问的公共HTTP api请求进行简单封装为http_client
class UserHttpClient(HttpClient):

    def __init__(self, api_root_url, **kwargs):
        super(UserHttpClient, self).__init__(api_root_url+"/user", **kwargs)

    #分页获取所有用户
    def get_all_uesr(self, **kwargs):
        return self.post("/getAllUser", **kwargs)

    #获取指定用户信息
    def get_user(self,**kwargs):
        return self.post("/getUser", **kwargs)
    # 用户更新基础信息
    def update_base_info(self, **kwargs):
        return self.post("/updateBaseInfo", **kwargs)

    # 用户更新密码
    def update_password(self, **kwargs):
        return self.post("/updatePassword", **kwargs)

    #添加用户
    def add_user(self,**kwargs):
        return self.post("/addUser", **kwargs)

    #删除用户
    def delete_user(self,**kwargs):
        return self.post("/deleteUser", **kwargs)

    # 用户注销
    def logoff(self, **kwargs):
        return self.post("/logoff", **kwargs)

    #获取用户角色信息
    def get_role(self,**kwargs):
        return self.post("/getRole", **kwargs)

    #更新用户拥有的角色信息
    def update_user_role_info(self,**kwargs):
        return self.post("/updateUser",**kwargs)

    #获取用户资源
    def get_resource(self, **kwargs):
        return self.post("/getResource", **kwargs)

user_http_client = UserHttpClient(api_root_url)