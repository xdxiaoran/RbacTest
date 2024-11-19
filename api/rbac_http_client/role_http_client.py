import os
from common.http_client import HttpClient
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

#对角色模块相关的需要控制访问的公共HTTP api请求进行简单封装为http_client
class RoleHttpClient(HttpClient):

    def __init__(self, api_root_url, **kwargs):
        super(RoleHttpClient, self).__init__(api_root_url+"/role", **kwargs)

    #分页获取所有角色
    def get_all_role(self, **kwargs):
        return self.get("/getAllRole", **kwargs)

    #获取指定角色
    def get_role(self, **kwargs):
        return self.post("/getRole", **kwargs)

    #添加角色
    def add_role(self,**kwargs):
        return self.post("/addRole", **kwargs)

    # 更新角色
    def update_role(self, **kwargs):
        return self.post("/updateRole", **kwargs)

    #删除角色
    def delete_role(self,**kwargs):
        return self.post("/deleteRole", **kwargs)

    #获取角色的所有用户
    def get_user_page(self,**kwargs):
        return self.post("/getUserPage", **kwargs)

    #获取角色的所有资源(按页)
    def get_resource_page(self, **kwargs):
        return self.post("/getResourcePage", **kwargs)

    # 获取角色的所有资源
    def get_resource_list(self, **kwargs):
        return self.post("/getResourceList", **kwargs)

    # 获取所有资源的列表
    def get_all_resource_list(self, **kwargs):
        return self.get("/getAllResourceList", **kwargs)

role_http_client = RoleHttpClient(api_root_url)