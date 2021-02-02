#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from Util.oper_Browser import Oper_browser
import time

class Tyzf:
    def __init__(self):
        self.driver=Oper_browser()
    def rever(self):
        self.driver.set_window_siz(200,400)

if __name__=="__main__":
    a=Tyzf()
    a.rever()