

import pytest
import allure
from common.logger import logger
from testcases.conftest import scenario_data, assert_results
from api.resource_api import  *
from common.mysql_operator import db

@allure.step("步骤1 ==>> 添加资源")
def step_1():
    logger.info("步骤1 ==>> 添加资源")

@allure.step("步骤2 ==>> 更新资源")
def step_2():
    logger.info("步骤2 ==>> 更新资源")

@allure.step("步骤3 ==>> 删除资源")
def step_3():
    logger.info("步骤3 ==>> 删除资源")


@allure.epic("针对业务场景的测试")
@allure.feature("场景：管理员操作资源添加-更新-删除")
class TestAdminResource():
    @allure.story("用例--管理员操作-资源添加-更新-删除")
    @pytest.mark.multiple
    def test_admin_resource_add_update_delete(self,get_admin_token_fixture):
        test_case=scenario_data['test_resource_role_add_update_delete']
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = add_resource(get_admin_token_fixture,test_case['add']['resourceName'],test_case['add']['code'],
                          test_case['add']['parentId'],test_case['add']['type'],test_case['add']['description'],test_case['add']['addPermissionList'])
        assert result.success is True,result.error
        resourceId=db.select_db(f"select id from resource where resource_name='{test_case['add']['resourceName']}'")[0]['id']
        print(resourceId)
        step_2()
        result=update_resource(get_admin_token_fixture,resourceId,test_case['update']['resourceName'],test_case['update']['code'],
                               test_case['update']['type'],test_case['update']['description'],test_case['update']['addPermissionList'])
        assert result.success is True,result.error
        step_3()
        result=delete_resource(get_admin_token_fixture,resourceId)
        assert_results(result, test_case['expect_result'], test_case['expect_code'], test_case['expect_msg'])
        logger.info("*************** 清理测试数据 ***************")
        db.execute_db(f"delete from resource where id={resourceId}")
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "test_04_admin_resource_add_update_delete.py"])