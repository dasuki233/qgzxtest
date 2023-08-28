# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：AddPositionPage.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/25 3:36 
'''
import logging
import time

import allure

from qgzxtest.common.BasePage import BasePage  # 导入基类
from qgzxtest.utils.screenshot_util import ScreenshotUtil


class AddPositionPage(BasePage):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.logger = logging.getLogger(__name__)  # 创建日志实例


    LOCATORS = {
        # 新增岗位二级菜单
        "position_icon": (
            'xpath', '''//li[text()="新增岗位"]'''),
        # 岗位名称
        "jobname_input": ('xpath', "//label[@for='jobname']/following-sibling::div/descendant::input"),
        # 限制人数
        "counts_input": ('xpath', "//label[@for='counts']/following-sibling::div/descendant::input"),
        # 截止时间年月日
        "date": ('xpath', "//label[@for='overTime']/following-sibling::div/descendant::input"),
        # 时间确定按钮
        "date_btn": ('xpath', """//div[@class="el-picker-panel__footer"]/button[contains(span, '确定')]"""),
        # 岗位介绍
        "description_input": ('xpath', "//label[@for='description']/following-sibling::div/descendant::textarea"),
        # 点击按钮
        'submit_button': ('xpath', "//div[@class='btns']/button[contains(span, '提交')]"),
        # 操作成功弹窗
        'submit_success_alert': ('xpath', "//html/body/div[@class='el-message el-message--success']/p[text()='操作成功!']")
    }

    def fill_form_and_submit(self, jobname, counts, date, description):
        '''
        :param jobname:岗位名称
        :param counts: 限制人数
        :param date: 截止日期
        :param description: 岗位介绍
        :return:None
        '''
        with allure.step("点击新建岗位菜单"):
            self.click(*self.LOCATORS['position_icon'])

        with allure.step("输入岗位名称"):
            allure.attach(f"输入岗位名称:{jobname}")
            self.send_keys(*self.LOCATORS["jobname_input"], value=jobname)

        with allure.step("输入限制人数"):
            allure.attach(f"输入限制人数:{counts}")
            self.clear(*self.LOCATORS["counts_input"])
            self.send_keys(*self.LOCATORS["counts_input"], value=counts)

        with allure.step("输入截止时间"):
            allure.attach(f"输入截止时间:{date}")
            self.send_keys(*self.LOCATORS["date"], value=date)
            self.sleep(1)
            self.click(*self.LOCATORS["date_btn"])  # 提交按钮的定位

        with allure.step("输入岗位介绍"):
            allure.attach(f"输入岗位介绍:{description}")
            self.send_keys(*self.LOCATORS["description_input"], value=description)
        screenshot_util = ScreenshotUtil(self.driver)  # 创建截图工具类实例
        screenshot_util.take_screenshot("submit")  # 调用截图方法，保存截图并添加到Allure报告中
        self.sleep(1)
        with allure.step("提交岗位信息"):
            self.click(*self.LOCATORS["submit_button"])  # 提交按钮的定位

    def get_assert_result(self):
        '''
        查询弹窗是否存在
        :return:Bool
        '''
        return self.is_element_exist(*self.LOCATORS['submit_success_alert'])

