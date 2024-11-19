

import pytest
import allure
from common.logger import logger
from testcases.conftest import scenario_data, assert_results
from api.role_api import *
from common.mysql_operator import db

@allure.step("步骤1 ==>> 添加角色")
def step_1():
    logger.info("步骤1 ==>> 添加角色")

@allure.step("步骤2 ==>> 更新角色")
def step_2():
    logger.info("步骤2 ==>> 更新角色")

@allure.step("步骤3 ==>> 删除角色")
def step_3():
    logger.info("步骤3 ==>> 删除角色")


@allure.epic("针对业务场景的测试")
@allure.feature("场景：管理员操作角色添加-更新-删除")
class TestAdminRole():
    @allure.story("用例--管理员操作-角色添加-更新-删除")
    # @allure.description("该用例是针对角色注册接口的测试")
    @pytest.mark.multiple
    def test_admin_role_add_update_delete(self,get_admin_token_fixture):
        test_case=scenario_data['test_admin_role_add_update_delete']
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = add_role(get_admin_token_fixture,test_case['add']['roleName'],test_case['add']['code'],
                          test_case['add']['parentId'],test_case['add']['description'],test_case['add']['addResourceList'])
        assert result.success is True,result.error
        roleId=db.select_db(f"select id from role where role_name='{test_case['add']['roleName']}'")[0]['id']
        step_2()
        result=update_role(get_admin_token_fixture,roleId,test_case['update']['roleName'],test_case['update']['code'],test_case['update']['description'],
                           test_case['update']['deleteResourceList'],test_case['update']['addResourceList'])
        assert result.success is True,result.error
        step_3()
        result=delete_role(get_admin_token_fixture,roleId)
        assert_results(result, test_case['expect_result'], test_case['expect_code'], test_case['expect_msg'])
        logger.info("*************** 清理测试数据 ***************")
        db.execute_db(f"delete from role where id={roleId}")
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_03_admin_role_add_update_delete.py"])
