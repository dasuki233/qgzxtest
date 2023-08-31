# 我的自动化测试练习
- 采用Page Object设计模式
- 由pytest、selenium、allure组成

# 效果图
添加效果图

# 环境准备
## 1. 安装python依赖模块
   - pip install -r requirements.txt
## 2. 安装allure
   - 下载allure： https://github.com/allure-framework/allure2/releases
## 3. 下载selenium
   - Microsoft Edge驱动器下载地址：http://selenium-release.storage.googleapis.com/index.html
   - Chrome驱动器下载地址：http://chromedriver.storage.googleapis.com/index.html
   - Firefox驱动器下载地址：https://github.com/mozilla/geckodriver/releases

# 修改配置
   - 将pages目录下BaseUtil.py的Service换成自己当前浏览器版本的驱动地址

# 项目结构
- common 基础方法类
- data 测试数据存放目录
- drivers selenium驱动器存放目录
- log 日志目录
- pages 存放页面元素和页面操作目录
- reports allure测试报告
- screenshots 存放测试产生的截图文件目录
- test_case 测试用例目录
- utils 公共方法
- all.py 执行测试用例生成报告

# 编码规范
- 统一使用python3.8
