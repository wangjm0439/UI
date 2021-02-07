#!/usr/bin/env python
# encoding: utf-8

import logging
import os
import time


def log():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)#Log等级总开关
    date=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    log_path=os.path.dirname(os.getcwd())+ '/Log/'
    log_name=log_path + date +'.log'
    log_f=logging.FileHandler(log_name,"w")
    #log_f.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    log_f.setFormatter(formatter)
    logger.addHandler(log_f)
    ch=logging.StreamHandler()
    #ch.setLevel(logging.WARNING)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
if __name__=="__main__":
    logger=log()
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')




