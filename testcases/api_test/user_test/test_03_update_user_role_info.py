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
class TestUpDateUserRoleInfo():
    @allure.story("用例--更新其他用户角色信息")
    @allure.description("该用例是针对更新其他用户角色信息接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,userId, deleteRoleList,addRoleList,expect_result,expect_code, expect_msg",
                             api_data["test_update_user_role_info"])
    def test_update_user_role_info(self,get_admin_token_fixture,get_test_user_token_fixture,get_nopri_user_fixture,
                                   token,userId,deleteRoleList,addRoleList,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="测试token":
            token=get_test_user_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = update_user_role_info(userId,token,deleteRoleList,addRoleList)
        if result.success:
            logger.info("*************** 清理数据 ***************")
            db.execute_db(f"delete  FROM `user_role` where user_id='{userId}'")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_03_update_user_role_info.py"])