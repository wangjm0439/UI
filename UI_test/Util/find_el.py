#!/usr/bin/env python
# encoding: utf-8
from Util.driver import driver

#查找元素并提交
def get_el(driver,method,el,keys=None):
    if method=='id':
        if keys==None:
            data=driver.find_element_by_id(el).click()
        else:
            data=driver.find_element_by_id(el).send_keys(keys)
    if method=='name':
        if keys==None:
            data=driver.find_element_by_name(el).click()
        else:
            data=driver.find_element_by_name(el).send_keys(keys)
    if method=='class_name':
        if keys==None:
            data=driver.find_element_by_class_name(el).click()
        else:
            data=driver.find_element_by_class_name(el).send_keys(keys)
    if method=='tag_name':
        if keys==None:
            data=driver.find_element_by_tag_name(el).click()
        else:
            data=driver.find_element_by_tag_name(el).send_keys(keys)
    if method=='link_text':
        if keys==None:
            data=driver.find_element_by_link_text(el).click()
        else:
            data=driver.find_element_by_link_text(el).send_keys(keys)
    if method=='partial_link_text':
        #超链接文本模糊匹配
        if keys==None:
            data=driver.find_element_by_partial_link_text(el).click()
        else:
            data=driver.find_element_by_partial_link_text(el).send_keys(keys)
    if method=='xpath':
        if keys==None:
            data=driver.find_element_by_xpath(el).click()
        else:
            data=driver.find_element_by_xpath(el).send_keys(keys)
    if method=='css_selector':
        if keys==None:
            data=driver.find_element_by_css_selector(el).click()
        else:
            data=driver.find_element_by_css_selector(el).send_keys(keys)
    return data

#查找元素是否存在
def if_el(driver,method,el):
    if method=='id':
        data=driver.find_element_by_id(el)
    if method=='name':
        data=driver.find_element_by_name(el)
    if method=='class_name':
        data=driver.find_element_by_class_name(el)
    if method=='tag_name':
        data=driver.find_element_by_tag_name(el)
    if method=='link_text':
        data=driver.find_element_by_link_text(el)
    if method=='partial_link_text':
        #超链接文本模糊匹配
        data=driver.find_element_by_partial_link_text(el)
    if method=='xpath':
        data=driver.find_element_by_xpath(el)
    if method=='css_selector':
        data=driver.find_element_by_css_selector(el)
    return data






