import pytest
import json

from common.operationJson import depend_list, read_json_file, write_json_file, depend_data_replace
from common.requestmethod import req
from common.operationExcel import OperationExcel, ExcelVariables
from common.assertFunction import assert_func
from common.logger import atp_log
from xlutils.copy import copy
from common.filepublic import filepath
from common.excelKeyWord import TestCaseKeyWord


class RequestHandler:
    def __init__(self, case):
        self.case = case
        # 读取json文件取出已有的参数
        self.load_dict = read_json_file('data', 'fa_test.json')

    def check_url(self, pytestconfig):
        # 第一步 处理URL-----------------------------------------------------------------------
        """
        @param value:   测试用例集
        @param host :   因为可能存在多个域名
        @param pytestconfig: 内置 fixture
        """
        # 替换url中的参数
        url = pytestconfig.getini('host_url') + self.case[ExcelVariables.url]
        url = depend_data_replace(url, self.load_dict)
        return url

    def check_param(self):
        # 第二步 处理参数  待处理------------------------------------------------------------------
        params = self.case[ExcelVariables.params]
        if len(str(params).strip()) == 0:
            pass
        elif len(str(params).strip()) > 0:
            if isinstance(params, dict):
                params = json.dumps(params, ensure_ascii=False)
            else:
                pass
        params = depend_data_replace(params, self.load_dict)
        return params

    def send_request(self, pytestconfig):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            'Accept': "application/json",
            # "Cookie": pytestconfig.getini('cookie')
            # 'Content-Type':'application/json'
        }
        method = self.case[ExcelVariables.method]
        url = self.check_url(pytestconfig)
        params = self.check_param()
        # 第三步 发送请求 -----------------------------------------------------------------------
        r = req.request(url=url, headers=header, params=params, method=method, verify=False)
        result = r.json()

        # 第四步 处理返回结果,写入json文件-------------------------------------------------------------------
        # 1/依赖返回数据,   2/依赖返回key值
        dep_data = self.case[ExcelVariables.depend_data]
        dep_key = self.case[ExcelVariables.depend_key]
        if dep_key:
            # 输出之后是这样的格式[{'amount_level_id': 99, 'amount_level_name': '待定'}],把depend_dcit存到json文件中
            load_dict2 = depend_list(dep_data, dep_key, result)
            write_json_file('data', 'fa_test.json', load_dict2)
        return result


# if __name__ == "__main__":
#     # obj = TestOrg()
#     pytest.main(['-s', 'test_03_funding.py'])
