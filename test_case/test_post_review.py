# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：test_post_review.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/31 18:09 
'''
import allure
import pytest

from qgzxtest.pages import LoginPage
from qgzxtest.pages.BaseUtil import BaseUtil
from qgzxtest.pages.PostReviewPage import PostReviewPage
from qgzxtest.utils.logger import logger
from qgzxtest.utils.read_data import ReadData


@allure.feature("岗位审查功能")
@allure.severity(allure.severity_level.CRITICAL)
class TestPostReview(BaseUtil):

    @allure.story("用例--查询功能测试")
    @allure.title("岗位审查-查询功能测试=>预期成功")
    @allure.description("该用例是查询岗位场景的测试")
    @allure.testcase("http://localhost:8080/admin/positionManagement/PostReview",
                     name="点击，跳转到岗位审查用例的链接地址")
    @pytest.mark.parametrize('data', ReadData().load_yaml('post_review_data.yml')['job_search'])
    def test_job_search(self, data):
        # 登录
        with allure.step("登录"):
            logger.info("*************** 开始执行岗位审查用例 ***************")
            lp = LoginPage.Login(self.driver)
            lp.login('admin', 'admin', '管理员')

        # 下面的代码都要登陆后才能操作
        with allure.step(f"查询岗位名称为:{data['jobname']}的数据"):
            post_review_opeartion = PostReviewPage(self.driver)  # 传递 driver 参数
            assert_total = post_review_opeartion.job_search(data['jobname'])  # 返回查询到有多少条数据
        logger.info('期望获得【{}】数据， 实际获得【{}】数据'.format(data['total'], assert_total))
        assert assert_total == data['total'], '数据不匹配'
        logger.info("*************** 结束执行岗位审查用例 ***************")

    @allure.story("用例--岗位审查操作")
    @allure.title("岗位审查-审核或删除=>预期成功")
    @allure.description("该用例是针对审核或删除岗位场景的测试")
    @allure.testcase("http://localhost:8080/admin/positionManagement/PostReview",
                     name="点击，跳转到岗位审查用例的链接地址")
    @pytest.mark.parametrize('data', ReadData().load_yaml('post_review_data.yml')['post_review_operation'])
    def test_post_review_operation(self, data):
        # 登录
        with allure.step("登录"):
            logger.info("*************** 开始执行岗位审查用例 ***************")
            lp = LoginPage.Login(self.driver)
            lp.login('admin', 'admin', '管理员')

            # 下面的代码都要登陆后才能操作
        with allure.step(f"对岗位进行{data['operation']}操作"):
            post_review_opeartion = PostReviewPage(self.driver)  # 传递 driver 参数
            assert_result = post_review_opeartion.job_operation(data['ID'], data['operation'])

        assert assert_result is True, '未操作成功'
        logger.info("*************** 结束执行岗位审查用例 ***************")
