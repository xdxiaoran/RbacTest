import pytest
import allure
from testcases.conftest import api_data
from api.resource_api import *
from common.mysql_operator import db
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("资源模块")
class TestDeleteResource():
    @allure.story("用例--删除资源")
    @allure.description("该用例是针对删除资源接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,resourceId,expect_result, expect_code, expect_msg",
                             api_data["test_delete_resource"])
    def test_delete_resource(self,get_admin_token_fixture,get_nopri_user_fixture,token,resourceId,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token == "管理员token":
            token = get_admin_token_fixture
        elif token == "无权限token":
            token = get_nopri_user_fixture
        result = delete_resource(token,resourceId)
        if result.success:
            logger.info("*************** 恢复用例状态 ***************")
            db.execute_db(f"update resource set is_delete=0 where id={resourceId}")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_05_delete_resource.py"])