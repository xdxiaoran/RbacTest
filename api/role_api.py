from api.rbac_http_client.role_http_client import role_http_client
from api.index_user_api import *

#role模块实际的业务功能，基于对应的httpclient实现

def get_all_role(token):
    """
    查询所有的角色
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type":"application/json",
        "token":token
    }
    res = role_http_client.get_all_role(headers=headers)
    genResulut(result, res)
    return result

def get_role(roleId,token):
    """
    查询指定角色
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "token":token
    }
    data={
        "roleId":roleId
    }
    res = role_http_client.get_role(headers=headers,data=data)
    genResulut(result, res)
    return result

def update_role(token,id,roleName,code,description,deleteResourceList=[],addResourceList=[]):
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
        "roleName":roleName,
        "code":code,
        "description":description,
        "deleteResourceList":deleteResourceList,
        "addResourceList": addResourceList
    }
    res = role_http_client.update_role(headers=headers,json=json)
    genResulut(result,res)
    return result

def add_role(token,roleName,code,parentId,description,addResourceList=[]):
    """
    添加角色
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token":token
    }
    json={
        "roleName":roleName,
        "code":code,
        "description":description,
        "parentId":parentId,
        "addResourceList": addResourceList
    }
    res = role_http_client.add_role(headers=headers,json=json)
    genResulut(result,res)
    return result

def delete_role(token,roleId):
    """
    删除角色
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token":token
    }
    params={
        "roleId":roleId
    }
    res = role_http_client.delete_role(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_user_page(token,roleId,pageNo=0,PageSize=5):
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
        "pageNo":pageNo,
        "pageSize":PageSize,
        "roleId": roleId
    }
    res = role_http_client.get_user_page(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_resource_page(token,roleId,pageNo=0,PageSize=5):
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
        "roleId":roleId
    }
    res = role_http_client.get_resource_page(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_resource_list(token,roleId):
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
        "roleId":roleId
    }
    res = role_http_client.get_resource_list(headers=headers,params=params)
    genResulut(result,res)
    return result

def get_all_resource_list(token):
    """
    获取所有资源列表
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "token":token
    }
    res = role_http_client.get_all_resource_list(headers=headers)
    genResulut(result,res)
    return result
# token=login("15320255643","15320255643").data['data']['token']
# print(get_all_role(token).data)
# print(add_role(token,"test","6666","超级管理员","testDes").data)
# print(update_role(token,1848613418682933249,"test","6666666","testDes").data)
# print(delete_role(token,1848613418682933249).data)
# print(get_user(token,1846079261643087873).data)
# print(get_resource(token,1846079261643087873).data)
