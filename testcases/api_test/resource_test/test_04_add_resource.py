import pytest
import allure
from common.logger import logger
from testcases.conftest import api_data
from api.resource_api import *
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("资源模块")
class TestAddResource():
    @allure.story("用例--新增资源")
    @allure.description("该用例是针对新增资源接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,resourceName,code,parentId,type,description,addPermissionList,expect_result, expect_code, expect_msg",
                             api_data["test_add_resource"])
    def test_add_resource(self,get_admin_token_fixture,get_nopri_user_fixture,token,resourceName,
                          code,parentId,type,description,addPermissionList,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token == "管理员token":
            token = get_admin_token_fixture
        elif token == "无权限token":
            token = get_nopri_user_fixture
        result = add_resource(token, resourceName,code,parentId,type,description,addPermissionList)
        if result.success:
            logger.info("*************** 清理用例 ***************")
            db.execute_db(f"delete from resource where resource_name='{resourceName}'")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_02_add_resource.py"])