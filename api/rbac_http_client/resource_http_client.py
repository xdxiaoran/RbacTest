import os
from common.http_client import HttpClient
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

#对资源模块相关的需要控制访问的公共HTTP api请求进行简单封装为http_client
class ResourceHttpClient(HttpClient):

    def __init__(self, api_root_url, **kwargs):
        super(ResourceHttpClient, self).__init__(api_root_url+"/resource", **kwargs)

    #获取所有资源
    def get_all_resource(self, **kwargs):
        return self.get("/getAllResource", **kwargs)

    # 获取指定资源
    def get_resource(self, **kwargs):
        return self.post("/getResource", **kwargs)

    # 更新资源
    def update_resource(self, **kwargs):
        return self.post("/updateResource", **kwargs)

    #添加资源
    def add_resource(self,**kwargs):
        return self.post("/addResource", **kwargs)


    #删除资源
    def delete_resource(self,**kwargs):
        return self.post("/deleteResource", **kwargs)

    #获取资源的所属角色
    def get_role(self,**kwargs):
        return self.post("/getRole", **kwargs)

    #获取资源的所有权限
    def get_permission(self, **kwargs):
        return self.post("/getPermission", **kwargs)

    # 获取所有资源
    def get_all_resource_list(self, **kwargs):
        return self.post("/getAllResourceList", **kwargs)

resource_http_client = ResourceHttpClient(api_root_url)