from api.rbac_http_client.user_http_client import user_http_client
from api.index_user_api import *
from api.index_user_api import genResulut

#user模块实际的业务功能，基于对应的httpclient实现

def get_all_user(token,pageNo=0,pageSize=5,name=None,gender=None,phone=None,email=None):
    """
    查询所有的用户
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token":token
    }
    params={
        "pageNo": pageNo,
        "pageSize": pageSize,
    }
    json={
        "name":name,
        "gender":gender,
        "phone":phone,
        "email":email
    }
    res = user_http_client.get_all_uesr(headers=headers,json=json,params=params)
    genResulut(result, res)
    return result

def get_user(token,id):
    """
             获取指定用户信息
             :return: 自定义的关键字返回结果 result
       """
    result = ResultBase()
    haeders={
        "Content-Type": "application/x-www-form-urlencoded",
        "token": token
    }
    data={
        "userId":id,
    }
    res=user_http_client.get_user(headers=haeders,data=data)
    genResulut(result, res)
    return result

def updata_base_info(id,userName,gender,phone,email,token):
    """
          用户更新个人信息（密码应传入加密后的密码，这里简单处理）
          :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    json = {
        "id":id,
        "userName":userName,
        "gender":gender,
        "phone":phone,
        "email":email
    }
    res = user_http_client.update_base_info(headers=headers,json=json)
    genResulut(result,res)
    return result

def updata_password(id,oldPassword,newPassword,token):
    """
          用户更新个人密码（密码应传入加密后的密码，这里简单处理）
          :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": token
    }
    data = {
        "userId":id,
        "oldPassword":get_rsa_ecode_password(oldPassword).data["data"],
        "newPassword":get_rsa_ecode_password(newPassword).data["data"]
    }
    res = user_http_client.update_password(headers=headers,data=data)
    genResulut(result,res)
    return result

def add_user(userName,phone,email,addRoleList,token):
    """
        添加用户
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    json={
        "userName": userName,
        "phone": phone,
        "email": email,
        "addRoleList": addRoleList
    }
    res = user_http_client.add_user(headers=headers, json=json)
    genResulut(result, res)
    return result

def delete_user(userId,token):
    """
        删除用户
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    params={
        "userId": userId,
    }
    res = user_http_client.delete_user(headers=headers, params=params)
    genResulut(result, res)
    return result
#需要保证当前用户处于登录状态
def logoff(uesrId,token):
    """
        用户登出
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": token
    }
    data = {
        "userId":uesrId
    }
    res = user_http_client.logoff(headers=headers, data=data)
    genResulut(result,res)
    return result
def get_role(userId,token):
    """
        获取用户角色信息
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/x-www-form-unlencoded",
        "token": token
    }
    params={
        "userId": userId,
    }
    res = user_http_client.get_role(headers=headers, params=params)
    genResulut(result, res)
    return result

def update_user_role_info(id,token,deleteRoleList=[],addRoleList=[]):
    """
        get_permission
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/json",
        "token": token
    }
    json={
        "id":id,
        "deleteRoleList": deleteRoleList,
        "addRoleList": addRoleList
    }
    res = user_http_client.update_user_role_info(headers=headers, json=json)
    genResulut(result, res)
    return result

def getResource(userId,token):
    """
        更新用户角色信息
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        "Content-Type": "application/x-www-form-unlencoded",
        "token": token
    }
    params = {
        "userId": userId,
    }
    res = user_http_client.get_resource(headers=headers, params=params)
    genResulut(result, res)
    return result

# token=login("15320255643","15320255643").data['data']['token']
# print(token)

#注意这里，接口错误，需要传数字
# print(get_all_user(token,gender=1).data)

# token=login('18592037348','18592037348').data['data']['token']
# print(update_user_own(1846795390791208961,'萧然','18592037348','男','18592037348','2312213qq.com',token).data)

# print(add_user('萧然2','18592037351','男','18592037351','2312213@qq.com',[],token).data)
# print(login(18592037351,18592037351).data)
# print(delete_user(login("18592037351","18592037351").data['data']['id'],token).data)
# print(get_role(1846795390791208961,token).data)
# print(update_user_role_info(1849351355764076546,token,[],[1846079261643087874]).data)
# print(getPermission(1846801442433683458,token).data)