#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver


def driver():
    # 加启动配置
    option = webdriver.ChromeOptions()
    # 关闭“chrome正受到自动测试软件的控制”
    # V75以及以下版本
    # option.add_argument('disable-infobars')
    # V76以及以上版本
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 不自动关闭浏览器
    option.add_experimental_option("detach", True)
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(10)#隐士等待10S
    return driver
if __name__=="__main__":
    driver().get("https://www.jianshu.com/")