import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from api.role_api import *
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("角色模块")
class TestGetAllRole():
    @allure.story("用例--获取指定角色")
    @allure.description("该用例是针对获取指定角色接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,roleId,expect_result,expect_code, expect_msg",
                             api_data["test_get_role_info"])
    def test_get_role(self,get_admin_token_fixture,get_test_user_token_fixture,get_nopri_user_fixture,token,roleId,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token == "管理员token":
            token = get_admin_token_fixture
        elif token == "无权限token":
            token = get_nopri_user_fixture
        elif token == "测试token":
            token = get_test_user_token_fixture
        result =get_role(roleId,token)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_02_get_role.py"])