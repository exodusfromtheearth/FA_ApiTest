# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:assertFunction.py
# Time:2021/1/19 7:00 下午
import json
from pytest_assume.plugin import assume


"""设置断言，状态码如果不正确会继续对期望结果断言；
但是如果期望结果第一个断言失败，将不会继续断言后面的期望结果"""


def assert_func(result, assert_code, assert_value):
    with assume: assert result['code'] == assert_code, "返回状态码不对"
    if assert_value:
        assert_list = assert_value.split(",")
        for i in assert_list:
            with assume: assert i in json.dumps(result, ensure_ascii=False), "断言失败%s" % result
