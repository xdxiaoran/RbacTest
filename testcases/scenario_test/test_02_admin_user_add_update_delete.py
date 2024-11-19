import pytest
import allure
from testcases.conftest import scenario_data, assert_results
from api.user_api import *
from common.mysql_operator import db

@allure.step("步骤1 ==>> 添加用户")
def step_1():
    logger.info("步骤1 ==>> 添加用户")

@allure.step("步骤2 ==>> 更新用户")
def step_2():
    logger.info("步骤2 ==>> 更新用户")

@allure.step("步骤3 ==>> 删除用户")
def step_3():
    logger.info("步骤3 ==>> 删除用户")


@allure.epic("针对业务场景的测试")
@allure.feature("场景：管理员操作用户添加-更新-删除")
class TestAdminUser():
    @allure.story("用例--管理员操作-用户添加-更新-删除")
    # @allure.description("该用例是针对用户注册接口的测试")
    @pytest.mark.multiple
    def test_admin_user_add_update_delete(self,get_admin_token_fixture):
        test_case=scenario_data['test_admin_user_add_update_delete']
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = add_user(test_case['add']['userName'],test_case['add']['phone'],test_case['add']['email'],
                          test_case['add']['addRoleList'],get_admin_token_fixture)
        assert result.success is True,result.error
        userId=login(test_case['add']['phone'],'123456789').data['data']['id']
        print(userId)
        step_2()
        result=update_user_role_info(userId,get_admin_token_fixture,test_case['update']['deleteRoleList'],test_case['update']['addRoleList'])
        assert result.success is True,result.error
        step_3()
        result=delete_user(userId,get_admin_token_fixture)
        assert_results(result, test_case['expect_result'], test_case['expect_code'], test_case['expect_msg'])
        logger.info("*************** 清理测试数据 ***************")
        db.execute_db(f"delete from user where id={userId}")
        # logger.info("*************** 结束执行用例 ***************

if __name__ == '__main__':
    pytest.main(["-q", "test_02_admin_user_add_update_delete.py"])
