# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：test_001.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/20 22:04 
'''

import allure
import pytest

from qgzxtest.pages import LoginPage
from qgzxtest.pages.BaseUtil import BaseUtil
from qgzxtest.utils.logger import logger
from qgzxtest.utils.read_data import ReadData  # 导入测试数据
from qgzxtest.utils.screenshot_util import ScreenshotUtil  # 导入截图工具类


@allure.feature("登录功能")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin(BaseUtil):

    @allure.story("用例--登录--预期登录成功")
    @allure.title("用户登录=>预期成功")
    @allure.description("该用例是针对 登录成功 场景的测试")
    @allure.testcase("http://localhost:8080/", name="点击，跳转到登录用例的链接地址")
    @pytest.mark.parametrize('data', ReadData().load_yaml('login_data.yml')['test_normal_login'])
    def test_normal_login(self, data):
        logger.info("*************** 开始执行登录成功用例 ***************")
        lp = LoginPage.Login(self.driver)
        lp.login(data['username'], data['password'], data['role'])

        # 进入首页就截图
        ele_find = lp.get_except_result()
        if ele_find:
            screenshot_util = ScreenshotUtil(self.driver)  # 创建截图工具类实例
            screenshot_util.take_screenshot("login_success")  # 调用截图方法，保存截图并添加到Allure报告中

        logger.info("期望结果：{}， 实际结果：【 {} 】".format("True", ele_find))

        logger.info("*************** 结束执行登录成功用例 ***************")
        assert ele_find is True, '没找到首页icon元素,登录可能失败'

    @allure.story("用例--登录--预期登陆失败")
    @allure.title("用户登录=>预期失败")
    @allure.issue("http://localhost:8080/", name="点击，跳转到登录BUG的链接地址")
    @allure.description("该用例是针对 登录失败 场景的测试")
    @pytest.mark.parametrize('data', ReadData().load_yaml('login_data.yml')['test_invalid_login'])
    def test_invalid_login(self, data):
        logger.info("*************** 开始执行登录失败用例 ***************")
        lp = LoginPage.Login(self.driver)
        lp.login(data['username'], data['password'], data['role'])

        # 使用等待警告框出现
        re = lp.is_alert()
        res = ''
        if re:
            res += lp.get_alert_text()
            # 处理警告框
            re.accept()  # 点击警告框的确定按钮
        # 登陆失败
        ele_find = lp.get_except_result()
        logger.info("期望结果：{}， 实际结果：【 {} 】".format("False", str(ele_find)))
        logger.info("期望结果：{}， 实际结果：【 {} 】".format("校验失败，用户名或密码错误！", str(res)))
        logger.info("*************** 结束执行登录失败用例 ***************")
        assert ele_find is False, '进入了首页,预期登录失败,但登陆成功了'
