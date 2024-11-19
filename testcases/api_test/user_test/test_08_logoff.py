import pytest
import allure
from common.logger import logger
from common.mysql_operator import db
from testcases.conftest import assert_results
from testcases.conftest import api_data
from api.user_api import logoff
from api.index_user_api import register
from api.index_user_api import login

# @allure.severity(allure.severity_level.TRIVIAL)

##有问题，先不测
@allure.epic("针对单个接口的测试")
@allure.feature("用户模块")
class TestLogout():
    @allure.story("用例--用户注销")
    @allure.description("该用例是针对用户注销接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,userId, expect_result, expect_code, expect_msg",
                             api_data["test_logoff"])
    def test_logout(self, get_test_user_token_fixture,token,userId, expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="测试token":
            token=get_test_user_token_fixture
        result = logoff(userId,token)
        if result.success:
            logger.info("*************** 成功执行后恢复该数据 ***************")
            db.execute_db(f"update user set is_delete=0 where id={userId}")
            db.execute_db(f"update user_role set is_delete=0 where user_id={userId}")
        assert_results(result, expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "test_08_logoff.py"])
