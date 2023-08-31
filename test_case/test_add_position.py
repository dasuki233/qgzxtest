# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：test_add_position.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/25 3:47 
'''
import allure
import pytest

from qgzxtest.pages import AddPositionPage, LoginPage
from qgzxtest.pages.BaseUtil import BaseUtil
from qgzxtest.utils.logger import logger
from qgzxtest.utils.read_data import ReadData


@allure.feature("新增岗位功能")
@allure.severity(allure.severity_level.CRITICAL)
class TestAddPosition(BaseUtil):

    @allure.story("用例--新增岗位--预期新增成功")
    @allure.title("新增岗位=>预期成功")
    @allure.description("该用例是针对新增岗位成功场景的测试")
    @allure.testcase("http://localhost:8080/admin/positionManagement/AddPosition/",
                     name="点击，跳转到新增岗位用例的链接地址")
    @pytest.mark.parametrize('data', ReadData().load_yaml('add_position_data.yml')['test_add_position'])
    def test_add_position_success(self, data):
        # 登录
        with allure.step("登录"):
            logger.info("*************** 开始执行新增岗位成功用例 ***************")
            lp = LoginPage.Login(self.driver)
            lp.login('admin', 'admin', '管理员')

            # 下面的代码都要登陆后才能操作
        with allure.step("填写新增岗位表单并提交"):
            add_position_page = AddPositionPage.AddPositionPage(self.driver)  # 传递 driver 参数
            add_position_page.fill_form_and_submit(data['jobname'], data['counts'], data['date'],
                                                   data['description'])
            # 判断是否弹出操作成功
        assert_result = add_position_page.get_assert_result()
        assert assert_result is True, '未提交成功'
        logger.info("*************** 结束执行新增岗位成功用例 ***************")

    @allure.story("用例--新增岗位--预期新增失败")
    @allure.title("新增岗位=>预期失败")
    @allure.testcase("http://localhost:8080/admin/positionManagement/AddPosition/",
                     name="点击，跳转到新增岗位用例的链接地址")
    @allure.description("该用例是针对新增岗位失败场景的测试")
    @pytest.mark.parametrize('data', ReadData().load_yaml('add_position_data.yml')['test_invalid_add_position'])
    def test_add_position_failure(self, data):
        logger.info("*************** 开始执行新增岗位失败用例 ***************")
        # 登录
        with allure.step("登录"):
            logger.info("*************** 开始执行新增岗位成功用例 ***************")
            lp = LoginPage.Login(self.driver)
            lp.login('admin', 'admin', '管理员')
        with allure.step("填写新增岗位表单并提交"):
            add_position_page = AddPositionPage.AddPositionPage(self.driver)  # 传递 driver 参数
            add_position_page.fill_form_and_submit(data['jobname'], data['counts'], data['date'], data['description'])
        assert_error_msg = add_position_page.get_assert_error()
        logger.info("期望结果：{}， 实际结果： {} ".format(data['expect_values'], assert_error_msg))
        assert assert_error_msg == data['expect_values'], '提示内容错误'
        logger.info("*************** 结束执行新增岗位失败用例 ***************")
