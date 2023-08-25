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
        "position_icon": ('xpath', '//*[@id="app"]/section/aside/ul/li[2]/ul/li/ul/li[1]'),  # 新增岗位二级菜单
        # 岗位名称
        "jobname_input": ('xpath', '//*[@id="app"]/section/section/main/div/div/div/form/div[1]/div/div[1]/input'),
        # 限制人数
        "counts_input": ('xpath', '//*[@id="app"]/section/section/main/div/div/div/form/div[2]/div/div/div/input'),
        # 岗位介绍
        "description_input": ('xpath', '//*[@id="app"]/section/section/main/div/div/div/form/div[5]/div/div/textarea'),
        # 截止时间年月日
        "date": ('xpath', '//*[@id="app"]/section/section/main/div/div/div/form/div[3]/div/div/input'),
        # 时间确定按钮
        "date_btn": ('xpath', '/html/body/div[2]/div[2]/button[2]'),
        # 点击按钮
        'submit_button': ('xpath', '//*[@id="app"]/section/section/main/div/div/div/form/div[6]/button[1]')
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
