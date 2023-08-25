# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：LoginPage.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/20 21:59 
'''
from selenium import webdriver

from qgzxtest.common.BasePage import BasePage


class Login(BasePage):
    # 登录元素
    _loc_username = ('xpath', '//*[@id="app"]/div/div[2]/div/div/form/div[1]/div/div[1]/input')  # 用户名
    _loc_password = ('xpath', '//*[@id="app"]/div/div[2]/div/div/form/div[2]/div/div[1]/input')  # 密码
    _loc_role = ('class_name', 'el-radio__input')  # 角色选择框
    _loc_btn = ('id', 'successBtn')  # 登录确定
    home_icon = ('css_selector', '.el-icon-s-home')  # 用于确定登录的,进入首页的icon

    role_dict = {
        '管理员': 0,
        '教师': 1,
        '学生': 2
    }

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)

    def login(self, username, password, role):
        # 输入动作 登录
        self.send_keys(*self._loc_username, username)
        self.send_keys(*self._loc_password, password)
        self.find_elements(*self._loc_role)[self.role_dict[role]].click()
        self.click(*self._loc_btn)  # 点击登录



    # 判断首页icon存在
    def get_except_result(self):
        return self.is_element_exist(*self.home_icon)
