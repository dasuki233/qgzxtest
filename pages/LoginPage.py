# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：LoginPage.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/20 21:59 
'''
import allure

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
        '''
        登录账号操作
        :param username: 账号
        :param password: 密码
        :param role: 登录角色(管理员、教师、学生）
        :return: None
        '''
        # 输入动作 登录
        with allure.step("输入账号"):
            allure.attach(f"输入账号:{username}")
            self.send_keys(*self._loc_username, value=username)
        with allure.step("输入密码"):
            allure.attach(f"输入密码:{password}")
            self.send_keys(*self._loc_password, value=password)
        with allure.step("选择登录角色"):
            allure.attach(f"选择登录角色:{role}")
            self.find_elements(*self._loc_role)[self.role_dict[role]].click()
        with allure.step("点击登录"):
            self.click(*self._loc_btn)  # 点击登录

    def get_except_result(self):
        '''
        判断首页icon存在
        :return: Bool
        '''
        return self.is_element_exist(*self.home_icon)
