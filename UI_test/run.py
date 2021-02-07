#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from Util.oper_Browser import *
from Util.find_el import *
import time

class Tyzf:
    def __init__(self):
        self.driver=driver()
    def rever(self,method,el):
        #self.driver.set_window_siz(200,400)
        get_url(self.driver,'https://www.cnblogs.com/fanqian0330/p/10723170.html')
        #time.sleep(10)
        get_el(self.driver,method,el)


if __name__=="__main__":
    a=Tyzf()
    a.rever('link_text',"新闻")