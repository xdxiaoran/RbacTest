import pytest
import allure
from common.logger import logger
from testcases.conftest import scenario_data, assert_results
from api.index_user_api import *
from api.user_api import *
from common.mysql_operator import db

@allure.step("步骤1 ==>> 注册用户")
def step_1():
    logger.info("步骤1 ==>> 注册用户")

@allure.step("步骤2 ==>> 登录用户")
def step_2():
    logger.info("步骤2 ==>> 登录用户")

@allure.step("步骤3 ==>> 更新用户")
def step_3():
    logger.info("步骤3 ==>> 更新用户")

@allure.step("步骤4 ==>> 登出用户")
def step_4():
    logger.info("步骤4 ==>> 登出用户")


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-登录-更新-登出")
class TestUser():
    @allure.story("用例--用户注册-登录-更新-登出")
    # @allure.description("该用例是针对用户注册接口的测试")
    @pytest.mark.multiple
    def test_user_register_login_update_logout(self):
        test_case=scenario_data['test_user_register_login_update_logout']
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = register(test_case['register']['userName'],test_case['register']['password'],
                          test_case['register']['gender'],test_case['register']['phone'],test_case['register']['email'])
        assert result.success is True,result.error
        step_2()
        result=login(test_case['login']['phone'],test_case['login']['password'])
        assert result.success is True,result.error
        userId=result.data['data']['id']
        token=result.data['data']['token']
        step_3()
        result=updata_base_info(userId,test_case['update']['userName'],
                               test_case['update']['gender'],test_case['update']['phone'],test_case['update']['email'],token)
        assert result.success is True,result.error
        step_4()
        result=logout(userId)
        assert_results(result, test_case['expect_result'], test_case['expect_code'], test_case['expect_msg'])
        logger.info("*************** 清理测试数据 ***************")
        db.execute_db(f"delete from user where id={userId}")
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_01_user_register_login_update_logout.py"])
