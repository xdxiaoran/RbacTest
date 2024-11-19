import json
from api.result_api import ResultBase
from api.rbac_http_client.index_user_http_client import index_user_http_client
from common.logger import logger

#index_user模块实际的业务功能，基于对应的httpclient实现

def genResulut(result,res):
    result.success = False
    if res.status_code ==200:
        if res.json()["code"] == 200:
            result.success = True
        result.data = res.json()
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
        logger.info(f"接口实际返回的结果为==>>{json.dumps(result.data, indent=4, ensure_ascii=False)}")
    else:
        result.error = "接口请求失败，状态码是 【 {} 】 ".format(res.status_code)
def get_publish_key():
    """
    获取公钥
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = index_user_http_client.get_publish_key()
    genResulut(result,res)
    return result

def get_rsa_ecode_password(pwd):
    """
    针对密码和公钥生成对应加密后的密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data={
        "password":pwd
    }
    res = index_user_http_client.get_rsa_ecode_password(headers=headers,data=data)
    genResulut(result,res)
    return result

def register(userName,password,gender,phone,email):
    """
    用户注册（实际后端接收的是加密后的密码，这里简单处理）
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/json"
    }
    json={
        "userName":userName,
        "password":get_rsa_ecode_password(password).data["data"],
        "gender":gender,
        "phone":phone,
        "email":email
    }
    res = index_user_http_client.register(headers=headers, json=json)
    genResulut(result,res)
    return result

def login(phone,password):
    """
        用户登录（实际后端接收的是加密后的密码，这里简单处理）
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "phone": phone,
        "password": get_rsa_ecode_password(password).data['data']
    }
    res = index_user_http_client.login(headers=headers, data=data)
    genResulut(result,res)
    return result

def logout(uesrId):
    """
        用户登出
        :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "userId":uesrId
    }
    res = index_user_http_client.logout(headers=headers, data=data)
    genResulut(result,res)
    return result





# print(get_publish_key().data)
# print(get_rsa_ecode_password('18592037349').data)
# print(get_publish_key().data)
# print(get_rsa_ecode_password('18592037349').data)
# print(register("萧然","18592037348","男","18592037348","62131232@qq.com").data)
# print(login("15320254462","15320254462").data['data']['token'])
# print(logout("1846801442433683458","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJyYmFjLXVzZXIiLCJpc3MiOiJsb25nY2hhbyIsImlhdCI6MTcyOTE1MjA3MSwiZXhwIjoxNzI5MTU1NjcxLCJpZCI6MTg0NjgwMTQ0MjQzMzY4MzQ1OH0.SNEb6dkZjvkJ_1wxbYUROzzW-xHZc2j4qfFqiqdCoSQ").data)