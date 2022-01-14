# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_02_org.py
# Time:2021/1/20 4:45 下午
import allure
import pytest
from common.assertFunction import assert_func
from common.operationExcel import OperationExcel, ExcelVariables
from common.requesthandler import RequestHandler


excel_obj = OperationExcel(1, 'data', 'api_common.xls')


@pytest.mark.all
class TestCase:
    @allure.feature("测试视频类型模块")
    @pytest.mark.parametrize("value", excel_obj.caserun())
    def test_03(self, value, pytestconfig):
        response = RequestHandler(value).send_request(pytestconfig)
        assert_code = value[ExcelVariables.expect_status_code]
        assert_value = value[ExcelVariables.expect]
        assert_func(response, assert_code, assert_value)


# if __name__ == '__main__':
#     pytest.main(['-s', 'test_01_company.py'])
