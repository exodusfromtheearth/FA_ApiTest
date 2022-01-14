
import pytest
from common.requesthandler import RequestHandler
from common.operationExcel import OperationExcel, ExcelVariables
from common.assertFunction import assert_func
import allure

'''跳过模块内所有测试用例'''
# pytestmark =pytest.mark.skip("no reason")


@pytest.fixture(scope="module")
def start():
    '''放置本模块内的前置操作'''
    print("前置操作")
    yield
    '''yiled之后放置用例执行完之后的操作，比如关闭数据库连接'''
    print("后置操作")


excel_obj_0 = OperationExcel(0, 'data', 'api_common.xls')
smokecaselist = excel_obj_0.casesmoke()
allcaselist = excel_obj_0.casesmoke()

smokecasenamelist = []
for i in smokecaselist:
    smokecasenamelist.append(i['描述'])
    
allcasenamelist = []
for i in allcaselist:
    allcasenamelist.append(i['描述'])


@pytest.mark.smoke
@allure.feature("测试机构模块的somke用例")
@pytest.mark.parametrize("smoke", smokecaselist, ids=smokecasenamelist)
def test_01(smoke, pytestconfig):
    response = RequestHandler(smoke).send_request(pytestconfig)
    assert_code = smoke[ExcelVariables.expect_status_code]
    assert_value = smoke[ExcelVariables.expect]
    assert_func(response, assert_code, assert_value)


@pytest.mark.all
@allure.feature("测试机构模块")
# @pytest.mark.skip("no reason")
class TestCase:
    @allure.story("测试机构-1用例")
    @pytest.mark.parametrize("org_1", allcaselist, ids=allcasenamelist)
    def test_03(self, org_1, pytestconfig):
        response = RequestHandler(org_1).send_request(pytestconfig)
        assert_code = org_1[ExcelVariables.expect_status_code]
        assert_value = org_1[ExcelVariables.expect]
        assert_func(response, assert_code, assert_value)

    @allure.story("测试机构-2用例")
    @pytest.mark.parametrize("org_2", smokecaselist, ids=smokecasenamelist)
    def test_01(self, org_2, pytestconfig):
        response = RequestHandler(org_2).send_request(pytestconfig)
        assert_code = org_2[ExcelVariables.expect_status_code]
        assert_value = org_2[ExcelVariables.expect]
        assert_func(response, assert_code, assert_value)


# if __name__ == "__main__":
    # pytest.main(['--alluredir', './report/report.html'])
    # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ./report/report.html -o ./report --clean')
    # pytest.main(['-s', 'test_00.py'])
    # pytest.main(['-s', 'test_00.py','-m=smoke'])
    # pytest.main(['-s', 'test_00.py','-m=not smoke'])

