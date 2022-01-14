# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:runall.py
# Time:2022/1/8 6:03 下午
import os
import pytest
from common.sendEmail import EmailHandler


if __name__ == '__main__':
    pytest.main('-m=all')
    EmailHandler().send_email()