import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from api.user_api import get_user
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户模块")
class TestGetUser():
    @allure.story("用例--获取指定用户信息")
    @allure.description("该用例是针对获取指定用户信息接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("userId, token, expect_result, expect_code, expect_msg",
                             api_data["test_get_user_info"])
    def test_get_user_info(self,get_admin_token_fixture,get_test_user_token_fixture,get_nopri_user_fixture, userId,token, expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="测试token":
            token=get_test_user_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = get_user(token,userId)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")




if __name__ == '__main__':
    pytest.main(["-q", "test_02_get_user.py"])
