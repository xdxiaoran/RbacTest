from api.rbac_http_client.resource_http_client import resource_http_client
from api.index_user_api import *

#resource模块实际的业务功能，基于对应的httpclient实现

def get_all_resource(token):
    """
    查询所有的资源
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "token":token
    }
    res = resource_http_client.get_all_resource(headers=headers)
    genResulut(result,res)
    return result

def get_resource(token,resourceId):
    """
    查询指定资源
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "token":token
    }
    params={
        "resourceId":resourceId
    }
    res = resource_http_client.get_resource(headers=headers,params=params)
    genResulut(result,res)
    return result

def update_resource(token,id,resourceName,code,type,description,permissionList=[]):
    """
    更新角色
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token":token
    }
    json={
        "id":id,
        "resourceName":resourceName,
        "code":code,
        "type":type,
        "description":description,
        "permissionList":permissionList
    }
    res = resource_http_client.update_resource(headers=headers,json=json)
    genResulut(result,res)
    return result

def add_resource(token,resourceName,code,parentId,type,description,addPermissionList=None):
    """
    添加资源
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token":token
    }
    json={
        "resourceName":resourceName,
        "code":code,
        "parentId":parentId,
        "type":type,
        "description":description,
        "addPermissionList":addPermissionList
    }
    res = resource_http_client.add_resource(headers=headers,json=json)
    genResulut(result,res)
    return result


def delete_resource(token,resourceId):
    """
    删除资源
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/x-www-form-unlencoded",
        "token":token
    }
    params={
        "resourceId":resourceId
    }
    res = resource_http_client.delete_resource(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_role(token,resourceId):
    """
    获取角色对应用户
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/x-www-form-unlencoded",
        "token":token
    }
    params={
        "resourceId":resourceId
    }
    res = resource_http_client.get_role(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_permission(token,resourceId):
    """
    获取角色的所有资源
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/x-www-form-unlencoded",
        "token":token
    }
    params={
        "resourceId":resourceId
    }
    res = resource_http_client.get_permission(headers=headers,params=params)
    genResulut(result, res)
    return result


# token=login("15320255643","15320255643").data['data']['token']
# # print(get_all_resource(token).data)
# print(add_resource(token,"test","6666",1846109800614629382,"test","testDes").data)
# # print(update_resource(token,1848621462443646977,"test","6666666","testDes","test").data)
# # print(delete_resource(token,1848621462443646977).data)
# # print(get_role(token,1846109800614629392).data)
# # print(get_permission(token,1846109800614629379).data)
