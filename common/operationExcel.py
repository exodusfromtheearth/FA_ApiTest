# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:operationExcel.py
# Time:2021/1/19 6:03 下午

# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from common.filepublic import filepath
from common.excelKeyWord import TestCaseKeyWord


class ExcelVariables:
    case_id = "caseID"
    case_name = "描述"
    is_execute = "是否执行"
    url = "请求地址"
    method = "请求方式"
    header = "请求头"
    params = "请求参数"
    case_depend = "请求依赖"    # case 依赖
    depend_data = "依赖返回的数据"   # "depend_data"
    depend_key = "数据依赖字段"     # "depend_key"
    expect = "期望结果"     # assert
    expect_status_code = "返回状态码"
    result = "实际结果"
    smoke = "用例级别"


class OperationExcel:
    def __init__(self, num, root, excelname):
        self.root = root
        self.excelname = excelname
        self.num = num
        self.book = xlrd.open_workbook(filepath(root, excelname))

    def getsheet(self):
        '''获取excel文件的第几张表格'''
        return self.book.sheet_by_index(self.num)

    def getrows(self):
        """获取总行数"""
        return self.getsheet().nrows

    def getcols(self):
        '''获取总列数'''
        return self.getsheet().ncols

    def getexceldatas(self):
        '''第一步获取所有测试用例'''
        runlist = list()
        title = self.getsheet().row_values(0)
        for row in range(1, self.getrows()):
            rowvalue = self.getsheet().row_values(row)
            runlist.append(dict(zip(title, rowvalue)))
        return runlist

    def caserun(self):
        '''第二步获取可执行的测试用例'''
        runlist = list()
        for item in self.getexceldatas():
            isrun = item[ExcelVariables.is_execute]
            if isrun == 'yes':
                runlist.append(item)
            else:
                pass
        return runlist

    def casesmoke(self):
        '''第三步获取smoke级别的测试用例'''
        runlist = list()
        for item in self.getexceldatas():
            isrun = item[ExcelVariables.smoke]
            if isrun == 'smoke':
                runlist.append(item)
            else:
                pass
        return runlist

    # 将返回的状态码和断言结果写入Excel
    def write_actual_return(self, assert_result, row):
        rb = self.book
        w_b = copy(rb)
        w_sheet = w_b.get_sheet(self.num)
        w_sheet.write(row, TestCaseKeyWord.result, assert_result)
        w_b.save(filepath(self.root, self.excelname))


# # 调试代码
# if __name__ == '__main__':
#     excel_obj = OperationExcel(0, 'data', 'api_common.xls')
#     excel_obj.write_actual_return("pass",1)
#     rb = excel_obj.book
#     wb = copy(rb)
#     w_sheet = wb.get_sheet(0)
#     for item in excel_obj.caserun():
#         case_id = item[ExcelVariables.case_id]
#         print(case_id)
#         print(type(case_id))
#         excel_obj.write_actual_return('200', "断言成功", case_id)
#         excel_obj.write_actual_return(w_sheet, '200', "断言成功", int(case_id))
#     wb.save(filepath('data', 'fa_test.xls'))
