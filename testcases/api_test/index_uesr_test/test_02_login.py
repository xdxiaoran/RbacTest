import pytest
import allure
from common.logger import logger
from testcases.conftest import assert_results
from testcases.conftest import api_data
from api.index_user_api import login

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户公共基础模块")
class TestLogin():
    @allure.story("用例--用户登录")
    @allure.description("该用例是针对用户登录接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("phone, password, expect_result, expect_code, expect_msg",
                             api_data["test_login"])
    def test_login(self, phone, password, expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login(phone,password)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")
if __name__ == '__main__':
    pytest.main(["-q", "test_02_login.py"])
