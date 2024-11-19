import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from api.user_api import *
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户模块")
class TestAddUser():
    @allure.story("用例--添加用户")
    @allure.description("该用例是针对添加用户接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,userName,phone,email,addRoleList,expect_result, expect_code, expect_msg",
                             api_data["test_add_user"])
    def test_add_user(self,get_admin_token_fixture,get_nopri_user_fixture
                    ,token,userName,phone,email,addRoleList,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = add_user(userName,phone,email,addRoleList,token)
        logger.info("*************** 成功执行后清理该数据 ***************")
        if result.success:
            db.execute_db(f"delete from user where phone={phone}")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_03_add_user.py"])
