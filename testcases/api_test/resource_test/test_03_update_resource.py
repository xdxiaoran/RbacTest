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
class TestUpdateResource():
    @allure.story("用例--更新资源")
    @allure.description("该用例是针对更新资源接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,id,resourceName,code,type,description,permissionList,expect_result, expect_code, expect_msg",
                             api_data["test_update_resource"])
    def test_update_resource(self,get_admin_token_fixture,get_nopri_user_fixture,token,id,resourceName,code,type,
                             description,permissionList,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token == "管理员token":
            token = get_admin_token_fixture
        elif token == "无权限token":
            token = get_nopri_user_fixture
        result = update_resource(token,id,resourceName,code,type,description,permissionList)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_03_update_resource.py"])