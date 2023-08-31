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

    import shutil


    def rmfile(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)  # 删除文件
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # 递归删除文件夹及其内容
        print(f'删除了{path}')


    rmfile('log')

    # 生成json临时文件
    # pytest.main(['-vs', './test_case/test_001_login.py', '--alluredir', './temp', '--clean-alluredir'])
    pytest.main(['-vs', './test_case', '-n=4', '--alluredir', './temp', '--clean-alluredir'])

    # 通过json文件生成allure报告
    os.system('allure generate ./temp -o ./reports --clean')
