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
class TestDeleteRole():
    @allure.story("用例--删除角色")
    @allure.description("该用例是针对删除角色接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,roleId,expect_result,expect_code, expect_msg",
                             api_data["test_delete_role"])
    def test_delete_role(self,get_admin_token_fixture,get_nopri_user_fixture,token,roleId,expect_result,expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = delete_role(token, roleId)
        if result.success:
            logger.info("*************** 恢复删除数据 ***************")
            db.select_db(f" update role set is_delete=0 where id={roleId}")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_04_delete_role.py"])