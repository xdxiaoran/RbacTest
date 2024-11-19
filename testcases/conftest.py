import os

import allure
import pytest

from common.logger import logger
from common.read_data import data
from api.index_user_api import login
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

base_data = data.load_yaml(os.path.join(BASE_PATH,"data","base_data.yml"))
api_data = data.load_yaml(os.path.join(BASE_PATH,"data","api_test.yml"))
scenario_data=data.load_yaml(os.path.join(BASE_PATH,"data","scenario_test.yml"))
def assert_results(result, expect_result, expect_code, expect_msg):
    """
    断言结果并记录日志。
    参数:
        result: 实际结果对象，应该包含success, error, data等属性。
        expect_result: 期望的成功状态。
        expect_code: 期望的返回code。
        expect_msg: 期望的返回message。
    """

    # 断言实际结果与期望结果相同
    assert result.success == expect_result, result.error
    if "接口请求失败" in result.error:
        assert False
    # 记录期望和实际结果
    logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(expect_code, result.data["code"]))
    logger.info("返回信息 ==>> 期望结果：{}， 实际结果：{}".format(expect_msg, result.data["message"]))
    # 进一步断言返回的code和message
    assert result.data["code"] == expect_code, "Expected code: {}, but got: {}".format(expect_code, result.data["code"])
    assert result.data["message"] == expect_msg, "Expected message: {}, but got: {}".format(expect_msg,
                                                                                            result.data["message"])

@allure.step("前置步骤 ==>> 获取管理员token")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 获取管理员token")

@allure.step("前置步骤 ==>> 获取测试用户token")
def step_first1():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 获取测试用户token")

@allure.step("前置步骤 ==>> 获取无权限用户token")
def step_first2():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 获取无权限用户token")

#前置处理器，获取管理员token
@pytest.fixture(scope='session')
def get_admin_token_fixture():
    step_first()
    phone = base_data["admin_user"]["phone"]
    password = base_data["admin_user"]["password"]
    loginInfo = login(phone,password)
    return loginInfo.data['data']['token']

#前置处理器，获取测试用户token
@pytest.fixture(scope='session')
def get_test_user_token_fixture():
    step_first1()
    phone = base_data["test_user"]["phone"]
    password = base_data["test_user"]["password"]
    loginInfo = login(phone,password)
    return loginInfo.data['data']['token']

#前置处理器，获取无权限用户token
@pytest.fixture(scope='session')
def get_nopri_user_fixture():
    step_first2()
    phone = base_data["nopri_user"]["phone"]
    password = base_data["nopri_user"]["password"]
    loginInfo = login(phone,password)
    return loginInfo.data['data']['token']

#前置处理器，测试用户登录
@pytest.fixture(scope='function')
def login_test_user_fixture():
    step_first()
    phone = base_data["test_user"]["phone"]
    password = base_data["test_user"]["password"]
    loginInfo = login(phone,password)
    return loginInfo.data['data']['token']



if __name__ == '__main__':
    print(base_data["admin_user"])