#!/usr/bin/env python
# encoding: utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#打开网址
def get_url(driver,url):
    driver.get(url)

#跳出iframe框架
#如果frame有id或name就是使用此方法switch_to_frame("name值")或switch_to_frame("id值")
'''
如果iframe没有name或id的话，则可以通过下面的方式定位：
#先定位到iframe
elementi= driver.find_element_by_class_name('APP-editor-iframe')
#再将定位对象传给switch_to_frame()方法
driver.switch_to_frame(elementi) 
'''
#跳转iframe
def get_iframe(driver,iframe_name):
    driver.switch_to_frame(iframe_name)


def out_iframe(driver):
    driver.switch_to.default_content()





#控制浏览器窗口
def set_window_siz(driver,width,high):
    driver.set_window_size(width,high)

#全屏显示
def max_window(driver):
    driver.maximize_window()

#前进
def forward(driver):
    driver.forward()

#后退
def back(driver):
    driver.back()

#ctrl +A 全选
def ctrl_a(element):
    element.send_keys(Keys.CONTROL + 'a')

#鼠标单击操作
def click(driver,element):
    ActionChains(driver).click(element).perform()

#鼠标双击操作
def double_click(driver,element):
    ActionChains(driver).double_click(element).perform()

#右键单击
def right_click(driver,element):
    ActionChains(driver).context_click(element).perform()

#鼠标移动
def move_el(driver,element):
    ActionChains(driver).move_to_element(element).perform()

#将目标一移动到二处
def move_el1toel2(driver,element1,element2):
    ActionChains(driver).drag_and_drop(element1,element2).perform()

#将目标一拖拽到指定的坐标下
def move_el1(driver,element,width,high):
    ActionChains(driver).click_and_hold(element).move_by_offset(width,high).release().perform()

#弹框操作，alert警告弹框
def alert_window(driver):
    alert=driver.switch_to_alert()
    #获取消息框文本
    print(alert.text)
    alert.accept()#关闭弹框,接受弹框

#确认消息弹框（confirm）
def confirm_window(driver):
    alert=driver.switch_to_alert()
    print(alert.text)
    alert.accept() #关闭弹框,接受弹框
    alert.dismiss() #关闭弹框,取消弹框

#提示消息对话框（prompt）
def prompt_window(driver,key):
    alert=driver.switch_to_alert()
    print(alert.text)
    alert.send_keys(key)#弹框输入内容
    alert.accept()  # 接受弹框



if __name__=="__main__":
    get_url('driver','url')

