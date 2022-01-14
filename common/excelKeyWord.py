# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:excelKeyWord.py
# Time:2021/1/19 6:16 下午


class TestCaseKeyWord:
    """
    定义测试用例关键字类
    """
    case_id = 0
    case_name = 1
    is_execute = 2
    url = 3
    method = 4
    header = 5
    data = 6
    case_depend = 7
    """case依赖"""
    case_depend_data = 8
    """依赖的返回数据"""
    field_depend = 9
    """数据依赖字段"""
    expect = 10
    expect_status_code = 11
    result = 13
    smoke = 12