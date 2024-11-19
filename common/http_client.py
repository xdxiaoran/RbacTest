import requests
import json as complexjson
from common.logger import logger
#基于requests对http相关基础方法如get、post等方法进行封装，如加入了日志信息
class HttpClient():

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session =requests.session()

    def get(self, url,headers=None, **kwargs):
        return self.request(url, "GET",headers=headers, **kwargs)

    def post(self, url,headers=None,data=None, json=None,**kwargs):
        return self.request(url, "POST", headers,data, json, **kwargs)

    def put(self, url, headers=None,data=None, json=None,**kwargs):
        return self.request(url, "PUT", headers, data, json, **kwargs)

    def delete(self, url,headers=None,data=None, json=None,**kwargs):
        return self.request(url, "DELETE", headers,data,json,**kwargs)


    def request(self, url, method, headers=None,data=None, json=None, **kwargs):
        url = self.api_root_url + url
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url,headers=headers,**kwargs)
        if method == "POST":
            return self.session.post(url, headers=headers ,data=data, json=json,**kwargs)
        if method == "PUT":
            return self.session.put(url, headers=headers, data=data,json=json,**kwargs)
        if method == "DELETE":
            return self.session.delete(url, headers=headers,data=data,json=json,**kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        if params:
            logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        if data:
            logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        if  json:
            logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        if  files:
            logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        if cookies:
            logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))