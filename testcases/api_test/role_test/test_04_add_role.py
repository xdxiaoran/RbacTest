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
class TestAddRole():
    @allure.story("用例--新增角色")
    @allure.description("该用例是针对新增角色接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,roleName,code,parentName,description,addResourceList,expect_result,expect_code, expect_msg",
                             api_data["test_add_role"])
    def test_add_role(self,get_admin_token_fixture,get_nopri_user_fixture,token,roleName,code,parentName,description,addResourceList,expect_result,expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = add_role(token,roleName,code,parentName,description,addResourceList)
        if result.success:
            logger.info("*************** 清理数据 ***************")
            db.execute_db(f"delete from role where role_name='{roleName}'")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_02_add_role.py"])