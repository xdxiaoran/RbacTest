import allure
import pytest

from common.logger import logger
from common.read_data import data
from api.index_user_api import login

#
# @allure.step("前置步骤 ==>> 获取测试用户，获取token")
# def step_first():
#     logger.info("******************************")
#     logger.info("前置步骤开始 ==>> 获取管理员token")
# #前置处理器，获取管理员token
# @pytest.fixture(scope='session')
# def get_admin_token_fixture():
#     step_first()
#     phone = base_data["admin_user"]["phone"]
#     password = base_data["admin_user"]["password"]
#     loginInfo = login(phone,password)
#     return loginInfo.data['data']['token']