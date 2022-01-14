# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:test_02_org.py
# Time:2021/1/20 4:45 下午
import allure
import pytest
from common.assertFunction import assert_func
from common.operationExcel import OperationExcel, ExcelVariables
from common.requesthandler import RequestHandler


@pytest.mark.all
@pytest.mark.parametrize('a,b,expect',
                         [(1,2,3),
                          (2,3,5),
                          (3,4,9)])
def test01(a,b,expect):
    assert a + b == expect


# if __name__ == '__main__':
#     pytest.main(['-s', 'test_02_org.py'])
