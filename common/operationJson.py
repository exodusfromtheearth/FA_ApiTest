# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:operationJson.py
# Time:2021/1/19 6:08 下午
import re
import json
import jsonpath
from common.filepublic import filepath


def depend_list(dep_value, dep_key, result):
    """
    @param dep_value: excel表格中的['depend_data']
    @param dep_key: excel表格中的['depend_key']
    @param result: 请求返回值r.json()
    @return: 把请求返回value和key组装成字典，然后apend到list中 返回depend_list
    """
    # 定义一个空list，用于存放组装好的list
    depend_data_list = list()
    dep_key_list = dep_key.split(",")
    dep_value_list = dep_value.split(",")

    # 发送请求，然后替换依赖中的参数，定义一个list存放所有请求后的依赖返回值
    value_list = list()

    for i in range(0, len(dep_key_list)):
        # 从请求result中获取依赖返回值，若果返回多个符合要求的值，则取第一个；如果想取所有值再进行特殊处理吧
        value = jsonpath.jsonpath(result, dep_value_list[i])[0]
        value_list.append(value)
    depend_data_list.append(dict(zip(dep_key_list, value_list)))
    return depend_data_list


def read_json_file(root, name):
    # 读取json文件
    with open(filepath(fileroot=root, filename=name), "r", encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        return load_dict


def write_json_file(root, name, dep_list):
    """
    # 1、先把已有的内容读出来，放入list
    # 2、list.append加入新的内容，如果已经存在的数据不会重复添加
    # 3、再调用方式删除替换原有内容保存
    @param root: 文件路径
    @param name: 文件名
    @param dep_list: 打算存入的新内容,request返回值
    """
    load_dict = read_json_file(root, name)
    load_dict.update(dep_list[0])
    with open(filepath(fileroot=root, filename=name), "w", encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)


def depend_data_replace(data, load_dict):
    """
    #用于把 URL 或者 请求参数 中的请求依赖&<> 替换为json文件中的返回值
    @param data:原始URL或者请求参数
    @param load_dict: json文件读取出来的字典
    @return: 把参数替换为json文件中的参数，然后返回最终的URL
    """
    if "$<" in data:
        if isinstance(data, dict):
            data = json.dumps(data)
        matcher1 = re.findall(r"\$<(.*?)>", data, re.I)
        if matcher1:
            # 如果url_key不为空，则说明存在需要替换的参数
            for i in matcher1:
                key1 = "$<" + i + ">"
                data = data.replace(key1, str(load_dict[i]))
    return data

