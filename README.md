# 我的自动化测试练习
- 采用Page Object设计模式
- 由pytest、pytest-xdist、selenium、allure组成
- python：3.8.3

# 一、环境准备
## 1. 安装python依赖模块
   - pip install -r requirements.txt
## 2. 安装allure
   - 下载allure： https://github.com/allure-framework/allure2/releases
## 3. 下载selenium
   - Microsoft Edge驱动器下载地址：http://selenium-release.storage.googleapis.com/index.html
   - Chrome驱动器下载地址：http://chromedriver.storage.googleapis.com/index.html
   - Firefox驱动器下载地址：https://github.com/mozilla/geckodriver/releases

# 二、修改配置
   - 将pages目录下BaseUtil.py的Service换成自己当前浏览器版本的驱动地址

