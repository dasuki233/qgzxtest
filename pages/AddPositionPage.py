# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：AddPositionPage.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/25 3:36 
'''
import time

from qgzxtest.common.BasePage import BasePage  # 导入基类


class AddPositionPage(BasePage):
    def __init__(self, timeout=30):
        super().__init__(timeout)

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
        'submit_button': ('xpath', "//div[@class='btns']/button[contains(span, '提交')]")
    }

    def fill_form_and_submit(self, jobname, counts, date, description):
        self.click(*self.LOCATORS['position_icon'])
        self.send_keys(*self.LOCATORS["jobname_input"], value=jobname)
        self.send_keys(*self.LOCATORS["counts_input"], value=counts)
        self.send_keys(*self.LOCATORS["date"], value=date)
        self.send_keys(*self.LOCATORS["description_input"], value=description)
        self.click(*self.LOCATORS["date_btn"])  # 提交按钮的定位
        time.sleep(10)
        self.click(*self.LOCATORS["submit_button"])  # 提交按钮的定位