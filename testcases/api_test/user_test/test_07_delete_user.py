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
class TestDeleteUser():
    @allure.story("用例--删除用户")
    @allure.description("该用例是针对删除用户接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,phone, expect_result,expect_code, expect_msg",
                             api_data["test_delete_user"])
    def test_delete_user(self,get_admin_token_fixture,get_nopri_user_fixture,token,phone,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        sql_res=db.select_db("select id from user where phone=" + phone)
        id=-1
        if sql_res:
            id=str(sql_res[0]["id"])
        if token=="管理员token":
            token=get_admin_token_fixture
        elif token=="无权限token":
            token=get_nopri_user_fixture
        result = delete_user(id,token)
        logger.info("*************** 恢复被删除用例状态 ***************")
        if result.success:
                db.execute_db(f"update user set is_delete=0 where id={id}")
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_07_delete_user.py"])
