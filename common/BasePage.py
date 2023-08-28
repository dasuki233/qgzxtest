# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace
@File    ：pages.py
@IDE     ：PyCharm
@Author  ：zjj
@Date    ：2023/8/18 22:50
'''
import os
import time

import allure
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait as WD

from qgzxtest.utils.logger import logger


class BasePage:
    def __init__(self, driver, timeout=3):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'css_selector': By.CSS_SELECTOR
        }
        self.driver = driver  # WebDriver 实例
        self._wait = WebDriverWait(driver, 10)
        self.outTime = timeout  # 设置超时时间，默认为 10 秒

    def take_screenshot(self, screenshot_name):
        screenshot_dir = 'screenshots'
        if not os.path.exists(screenshot_dir):
            os.mkdir(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, screenshot_name + ".png")
        print(screenshot_path)
        self.driver.save_screenshot(screenshot_path)
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)

    def find_element(self, by, locator):
        """
        封装定位单个元素的方法
        :param by: 元素定位方式，例如 id、name、xpath、css 等
        :param locator: 具体的定位表达式
        :return: 定位到的单个元素对象
        """
        if by.lower() in self.byDic:
            try:
                # logger.info('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
                logger.info('[Info:开始通过 "{}" 查找元素 "{}"!]'.format(by, locator))
                element = WD(self.driver, self.outTime).until(lambda x: x.find_element(self.byDic[by], locator))
            except TimeoutException as t:
                # logger.error('error: found "{}" timeout! Timeout exception: "{}"'.format(locator, t))
                logger.error('error: 查找 "{}" 超时！超时异常: "{}" '.format(locator, t))
            else:
                return element

    def find_elements(self, by, locator):
        """
        封装定位一组元素的方法
        :param by: 元素定位方式，例如 id、name、xpath、css 等
        :param locator: 具体的定位表达式
        :return: 定位到的一组元素对象
        """
        if by.lower() in self.byDic:
            try:
                # logger.info('[Info:start find the elements {} by {}!]'.format(locator, by))
                logger.info('[Info:开始通过 "{}" 查找元素(elements) "{}"!]'.format(by, locator))
                elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(self.byDic[by], locator))
            except TimeoutException as t:
                # logger.error('error: found "{}" timeout! Timeout exception: "{}"'.format(locator, t))
                logger.error('error: 查找 "{}" 超时！超时异常: "{}"'.format(locator, t))
            else:
                return elements

    def is_element_exist(self, by, locator):
        """
        封装判断元素是否存在的方法
        :param by: 元素定位方式，例如 id、name、xpath、css 等
        :param locator: 具体的定位表达式
        :return: 若元素存在返回 True，否则返回 False
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime).until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                # logger.error('Error: Element "{}" does not exist'.format(locator))
                logger.error('Error: 元素 "{}" 不存在'.format(locator))
                return False
            return True
        else:
            # logger.error('Error: Invalid locator "{}"'.format(by))
            logger.error('Error: 无效的定位方式 "{}"'.format(by))

    def is_click(self, by, locator):
        # 封装判断元素是否可点击的
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime).until(ec.element_to_be_clickable((self.byDic[by], locator)))
                # logger.info('Element "{}" is clickable'.format(locator))
                logger.info('元素 "{}" 可点击'.format(locator))
            except TimeoutException:
                # logger.error('Element "{}" is not clickable'.format(locator))
                logger.error('元素 "{}" 不可点击'.format(locator))
            else:
                return element
        else:
            # logger.error('Invalid locator "{}"'.format(by))
            logger.error('无效的定位方式 "{}"'.format(by))

    def is_alert(self):
        """
        assert alert if exsit
        :return: alert obj
        """
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
            # logger.info('Alert found: {}'.format(re.text))
            logger.info('发现警告框: {}'.format(re.text))
        except (TimeoutException, NoAlertPresentException):
            # logger.error('No alert found')
            logger.error('未找到警告框')
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        # logger.info('Switching to iframe "{}"'.format(locator))
        logger.info('切换到iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
                # logger.info('Switched to iframe "{}" successfully'.format(locator))
                logger.info('成功切换到iframe "{}"'.format(locator))
            except TimeoutException as t:
                # logger.error('Failed to switch to iframe "{}". Timeout exception: {}'.format(locator, t))
                logger.error('无法切换到iframe "{}"。超时异常: {}'.format(locator, t))
        else:
            # logger.error('Invalid locator "{}"'.format(by))
            logger.error('无效的定位方式 "{}"'.format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        logger.info('切换回默认iframe')
        # logger.info('Switching back to default iframe')
        try:
            self.driver.switch_to.default_content()
            logger.info('成功切换回默认iframe')
            # logger.info('Switched back to default iframe successfully')
        except Exception as e:
            logger.error('无法切换回默认iframe。异常: {}'.format(e))
            # logger.error('Failed to switch back to default iframe. Exception: {}'.format(e))

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            alert_text = alert.text
            logger.info('获取警告框文本: {}'.format(alert_text))
            # logger.info('Got alert text: {}'.format(alert_text))
            return alert_text
        else:
            logger.warning('未找到警告框')
            # logger.warning('No alert found')
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            if name:
                attribute_value = element.get_attribute(name)
                # logger.info('Got attribute "{}" value: {}'.format(name, attribute_value))
                logger.info('获取属性 "{}" 的值: {}'.format(name, attribute_value))
                return attribute_value
            else:
                element_text = element.text
                # logger.info('Got element text: {}'.format(element_text))
                logger.info('获取元素文本: {}'.format(element_text))
                return element_text
        except AttributeError:
            # logger.error('Failed to get text from element "{}"'.format(locator))
            logger.error('无法从元素 "{}" 获取文本'.format(locator))
            return None

    def load_url(self, url):
        """加载url"""
        # logger.info('Loading URL: {}'.format(url))
        logger.info('正在加载网址: {}'.format(url))
        self.driver.get(url)

    def get_source(self):
        """获取页面源码"""
        # logger.info('Getting page source')
        logger.info('正在获取页面源代码')
        return self.driver.page_source

    def send_keys(self, by, locator, value=''):
        """写数据"""
        # logger.info('Input data: "{}" to element located by "{}" using "{}"'.format(value, locator, by))
        logger.info('向定位方式 "{}" 为 "{}" 的元素输入数据: "{}"'.format(by, locator, value))
        try:
            element = self.find_element(by, locator)
            # 添加等待，等待元素可交互
            WebDriverWait(self.driver, self.outTime).until(EC.element_to_be_clickable((by, locator)))
            element.send_keys(value)
        except AttributeError as e:
            # logger.error('Error while sending keys: {}'.format(e))
            logger.error('发送数据时出错: {}'.format(e))

    def clear(self, by, locator):
        """清理数据"""
        # logger.info('Clearing data in element located by "{}" using "{}"'.format(locator, by))
        logger.info('正在清理定位方式 "{}" 为 "{}" 的元素中的数据'.format(by, locator))
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            # logger.error('Error while clearing data: {}'.format(e))
            logger.error('清理数据时出错: {}'.format(e))


    def click(self, by, locator):
        """点击某个元素"""
        # logger.info('Clicking element located by "{}" using "{}"'.format(locator, by))
        logger.info('点击定位方式 "{}" 为 "{}" 的元素'.format(by, locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            # logger.warning('Element located by "{}" using "{}" is unclickable!'.format(locator, by))
            logger.warning('无法点击定位方式 "{}" 为 "{}" 的元素！'.format(locator, by))

    @staticmethod
    def sleep(num=0):
        """强制等待"""
        # logger.info('Forcing sleep for "{}" second'.format(num))
        logger.info('强制休眠 "{}" 秒'.format(num))

        time.sleep(num)

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        # logger.info('Waiting for element located by "{}" using "{}" to be located'.format(locator, by))
        logger.info('等待定位方式 "{}" 为 "{}" 的元素被定位'.format(by, locator))
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            # logger.error('Timeout error: Element located by "{}" using "{}" not located! "{}'.format(locator, by, t))
            logger.error('超时错误: 未定位到定位方式 "{}" 为 "{}" 的元素！ {}'.format(by, locator, t))

    def get_page_source(self):
        # logger.info('Getting page source')
        logger.info('正在获取页面源代码')
        return self.get_source()
