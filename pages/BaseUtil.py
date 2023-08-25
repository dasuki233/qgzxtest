# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：BaseUtil.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/21 17:21 
'''
import pytest
from selenium import webdriver

from qgzxtest.common.BasePage import BasePage
from qgzxtest.pages import LoginPage


class BaseUtil:
    def setup(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载网页
        self.driver.get('http://127.0.0.1:8080')


    def teardown(self) -> None:
        self.driver.quit()

