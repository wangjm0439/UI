#!/usr/bin/env python
# encoding: utf-8
from Util.driver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Oper_browser:
    def __init__(self):
        self.driver=driver()
    #打开网址
    def get_url(self,url):
        self.driver.get(url)

    #id查找元素，提交或点击
    def find_id(self,id,key=None):
        if key==None:
            self.driver.find_element_by_id().click()
        else:
            self.driver.find_element_by_id().send_keys(key)

    #id 查找元素是否存在
    def find_id_if(self,id):
        flag=True
        if self.driver.find_element_by_id(id):
            flag=True
        else:
            flag=False

    #通过name查找元素
    def find_name(self,name=None):

        self.driver.find_element_by_name(name)





    #控制浏览器窗口
    def set_window_siz(self,width,high):
        self.driver.set_window_size(width,high)

    #全屏显示
    def max_window(self):
        self.driver.maximize_window()

    #前进
    def forward(self):
        self.driver.forward()

    #后退
    def back(self):
        self.driver.back()

    #ctrl +A 全选
    def ctrl_a(self,element):
        element.send_keys(Keys.CONTROL + 'a')

    #鼠标单击操作
    def click(self,element):
        ActionChains(self.driver).click(element).perform()

    #鼠标双击操作
    def double_click(self,element):
        ActionChains(self.driver).double_click(element).perform()

    #右键单击
    def right_click(self,element):
        ActionChains(self.driver).context_click(element).perform()

    #鼠标移动
    def move_el(self,element):
        ActionChains(self.driver).move_to_element(element).perform()

    #将目标一移动到二处
    def move_el1toel2(self,element1,element2):
        ActionChains(self.driver).drag_and_drop(element1,element2).perform()

    #将目标一拖拽到指定的坐标下
    def move_el1(self,element,width,high):
        ActionChains(self.driver).click_and_hold(element).move_by_offset(width,high).release().perform()

    #弹框操作，alert警告弹框
    def alert_window(self):
        alert=self.driver.switch_to_alert()
        #获取消息框文本
        print(alert.text)
        alert.accept()#关闭弹框,接受弹框

    #确认消息弹框（confirm）
    def confirm_window(self):
        alert=self.driver.switch_to_alert()
        print(alert.text)
        alert.accept() #关闭弹框,接受弹框
        alert.dismiss() #关闭弹框,取消弹框

    #提示消息对话框（prompt）
    def prompt_window(self,key):
        alert=self.driver.switch_to_alert()
        print(alert.text)
        alert.send_keys(key)#弹框输入内容
        alert.accept()  # 接受弹框



if __name__=="__main__":
    op=Oper_browser()
    #op.set_window_siz(480,800)
    op.click()

