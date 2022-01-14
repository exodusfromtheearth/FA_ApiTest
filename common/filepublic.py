# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:filepublic.py
# Time:2021/1/19 6:06 下午
import os


def filepath(fileroot="data", filename="test.yaml"):
    pre_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(
        os.path.abspath(pre_dir), fileroot, filename)
