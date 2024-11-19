import pytest
import allure
from common.logger import logger
from testcases.conftest import assert_results
from testcases.conftest import api_data
from api.index_user_api import logout
from api.index_user_api import login

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户公共基础模块")
class TestLogout():
    @allure.story("用例--用户登出")
    @allure.description("该用例是针对用户登出接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("userId, expect_result, expect_code, expect_msg",
                             api_data["test_logout"])
    def test_logout(self, login_test_user_fixture,userId, expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = logout(userId)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_03_logout.py"])
