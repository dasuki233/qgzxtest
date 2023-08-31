# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：PostReviewPage.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/31 15:11 
'''

import allure

from qgzxtest.common.BasePage import BasePage  # 导入基类
from qgzxtest.utils.screenshot_util import ScreenshotUtil


class PostReviewPage(BasePage):
    def __init__(self, timeout=30):
        super().__init__(timeout)

    # 岗位审查二级菜单
    PUBLIC_MENU = {"post_review": ('xpath', '''//li[text()="岗位审查"]'''), }
    # 查询框测试
    SEARCH_LOCATORS = {
        # 岗位搜索框
        'search': ('xpath', "//input[@type='text' and @class='el-input__inner' and @placeholder='请输入岗位名称']"),
        # 查询按钮
        'search_button': ('xpath', "//button[span[text()='查询']]"),
        # 重置按钮
        'reset_button': ('xpath', "//button[span[text()='重置']]"),
        # 页面数据
        'page_data': ('class_name', "el-table__row"),
    }


    def job_search(self, jobname):
        '''
        模糊查询功能测试
        :param jobname:岗位名称
        :return:返回页面有多少条数据,与实际做的对比
        '''
        with allure.step("点击岗位审查菜单"):
            self.click(*self.PUBLIC_MENU['post_review'])
        with allure.step("输入岗位名称"):
            allure.attach(f"输入限制人数:{jobname}")
            self.send_keys(*self.SEARCH_LOCATORS['search'], value=jobname)
        with allure.step("点击查询按钮"):
            self.click(*self.SEARCH_LOCATORS['search_button'])
        with allure.step("查看获取了多少条数据"):
            total = str(len(self.find_elements(*self.SEARCH_LOCATORS['page_data'])))
            allure.attach(f":查询到【{total}】条数据")
        screenshot_util = ScreenshotUtil(self.driver)  # 创建截图工具类实例
        screenshot_util.take_screenshot("job_operation")  # 调用截图方法，保存截图并添加到Allure报告中
        return total

    def job_operation(self, ID, operation):
        '''
        对岗位进行操作
        :param ID:岗位ID
        :param opeartion:岗位操作
        :return:bool
        '''
        # 操作审核
        OPERATION = {
            # 审核
            'audit_button': ("xpath",
                             f"//tr[@class='el-table__row']/td[1][div/text()={ID}]//following-sibling::td//button/span[contains(text(), '审 核')]"),
            # 删除
            'delete_button': ("xpath",
                              f"//tr[@class='el-table__row']/td[1][div/text()={ID}]//following-sibling::td//button/span[contains(text(), '删 除')]"),
            # 审核选择弹窗
            'audit_alert': ("xpath", "//div[@class='el-popover el-popper' and @aria-hidden='false']"),
            # 审核不通过 or 不删除
            'audit_unpass': ("xpath", "//div[@class='el-popover el-popper' and @aria-hidden='false']//button[1]"),
            # 审核通过 or 删除
            'audit_pass': ("xpath", "//div[@class='el-popover el-popper' and @aria-hidden='false']//button[2]"),
            # 申请状态(用来检测是否审核成功)
            # "state": ('xpath', "//table//tr/td[5]"),
            "state": (
            'xpath', f"//tr[@class='el-table__row']/td[1][div/text()={ID}]/following-sibling::td[4]/div/span"),
            # 操作成功
            'submit_success': (
                'xpath', "/html/body/div[@class='el-message el-message--success is-closable' ]/p[text()='操作成功!']")
        }

        with allure.step("点击岗位审查菜单"):
            self.click(*self.PUBLIC_MENU['post_review'])
        with allure.step("修改前的状态"):
            initial_state = self.get_element_text(*OPERATION['state'])
            allure.attach(f"修改前的状态:{initial_state}")

        with allure.step(f"对ID为{ID}的岗位进行{operation}操作"):
            if operation in ['审核通过', '删除岗位']:
                self.click(*OPERATION['audit_button'])
                self.click(*OPERATION['audit_pass'])
            elif operation in ['审核不通过', '不删除岗位']:
                self.click(*OPERATION['audit_button'])
                self.click(*OPERATION['audit_unpass'])

        with allure.step("修改后的状态"):
            updated_state = self.get_element_text(*OPERATION['state'])
            allure.attach(f"修改后的状态:{updated_state}")
        screenshot_util = ScreenshotUtil(self.driver)  # 创建截图工具类实例
        screenshot_util.take_screenshot("job_operation")  # 调用截图方法，保存截图并添加到Allure报告中
        return self.is_element_exist(*OPERATION['submit_success'])
