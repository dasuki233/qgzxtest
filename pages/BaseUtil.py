# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：BaseUtil.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/21 17:21 
'''
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from qgzxtest.common.BasePage import BasePage
from qgzxtest.pages import LoginPage
from qgzxtest.utils.logger import logger


class BaseUtil:
    def setup(self) -> None:
        # self.driver = webdriver.Chrome()
        s = Service(os.path.dirname(__file__).split('pages')[0] + '/drivers/' + 'msedgedriver116.0.1938.62.exe')
        self.driver = webdriver.Edge(service=s)
        driver = self.driver
        # 加载网页
        # 最大化浏览器窗口
        driver.maximize_window()
        self.driver.get('http://127.0.0.1:8080')



    def teardown(self) -> None:
        self.driver.quit()

# s = Service(os.path.dirname(__file__).split('pages')[0] + '/drivers/' + 'msedgedriver116.0.1938.62.exe')
# driver = webdriver.Edge(service=s)
# driver.get('https://www.baidu.com/')