# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：all.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/4/13 19:08 
'''
import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-vs', './test_case', '-n=2'])  # 多线程
    # pytest.main(['-vs', './test_case', '--reruns=2'])  # 多次执行
    # pytest.main(['-vs', './test_case'])
    # 生成json临时文件
    pytest.main(['-vs', './test_case', '--alluredir', './temp', '--clean-alluredir'])

    # 通过json文件生成allure报告
    os.system('allure generate ./temp -o ./reports --clean')