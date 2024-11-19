import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from api.index_user_api import register
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户公共基础模块")
class TestRegitser():
    @allure.story("用例--用户注册")
    @allure.description("该用例是针对用户注册接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("userName, password, gender, phone, email, expect_result, expect_code, expect_msg",
                             api_data["test_register"])
    def test_register(self, userName, password, gender, phone, email, expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = register(userName, password, gender, phone, email)
        logger.info("*************** 成功执行后清理该数据 ***************")
        if result.success:
            db.execute_db(f"delete from user where phone={phone}")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_01_register.py"])
