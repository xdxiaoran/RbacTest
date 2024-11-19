import pytest
import allure
from testcases.conftest import api_data
from api.user_api import *
from testcases.conftest import assert_results

# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户模块")
class TestUpdatePassword():
    @allure.story("用例--用户更新个人密码")
    @allure.description("该用例是针对用户更新个人密码接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("token,UserId,oldPassword,newPassword, expect_result,expect_code, expect_msg",
                             api_data["test_update_password"])
    def test_update_password(self,get_test_user_token_fixture,get_admin_token_fixture,get_nopri_user_fixture,token,UserId
                              ,oldPassword,newPassword,expect_result, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        if token=="测试token":
            token=get_test_user_token_fixture
        if token=="管理员token":
            token=get_admin_token_fixture
        if token=="无权限token":
            token=get_nopri_user_fixture
        result = updata_password(UserId,oldPassword,newPassword,token)
        assert_results(result,expect_result, expect_code, expect_msg)
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_05_update_Password.py"])