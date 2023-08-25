# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：screenshot_util.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/24 3:23 
'''
import os
from selenium import webdriver
from qgzxtest.utils.logger import logger
import allure

class ScreenshotUtil:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, screenshot_name):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir = os.path.join(base_path, "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, screenshot_name + ".png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        logger.info('Screenshot saved: {}'.format(screenshot_path))
