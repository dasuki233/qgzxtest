# # -*- coding: UTF-8 -*-
# '''
# @Project ：Python_Workspace
# @File    ：test.py
# @IDE     ：PyCharm
# @Author  ：zjj
# @Date    ：2023/8/19 16:07
# '''
# from time import sleep
#
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait as WD
#
#
# def is_element_exist(by, locator):
#     """
#     封装判断元素是否存在的方法
#     :param by: 元素定位方式，例如 id、name、xpath、css 等
#     :param locator: 具体的定位表达式
#     :return: 若元素存在返回 True，否则返回 False
#     """
#     byDic = {
#         'id': By.ID,
#         'name': By.NAME,
#         'class_name': By.CLASS_NAME,
#         'xpath': By.XPATH,
#         'link_text': By.LINK_TEXT,
#         'css_selector': By.CSS_SELECTOR
#     }
#     outTime = 10
#     if by.lower() in byDic:
#         try:
#             WD(driver, outTime).until(ec.visibility_of_element_located((byDic[by], locator)))
#         except TimeoutException:
#             print('Error: Element "{}" does not exist'.format(locator))
#             return False
#         return True
#     else:
#         print('Error: Invalid locator "{}"'.format(by))
#
#
# driver = webdriver.Chrome()
# driver.get("http://localhost:8080/Home")
# print(is_element_exist('css_selector', ".el-icon-s-home"))
# sleep(100)
import os

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件和子目录
for root, dirs, files in os.walk(current_directory):
    print(f"当前目录：{root}")
    print("子目录：", dirs)
    print("文件：", files)
    print("=" * 40)
