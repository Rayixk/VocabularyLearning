# encoding: utf-8
# !/usr/bin/env python
# __author__ = "yang"
# Date: 2017/6/22


import logging
import os


def getlogger(name, logfile):
    os.makedirs(os.path.dirname(logfile), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 创建一个handler,用于写入日志文件输出控制台
    fh = logging.FileHandler(logfile,encoding="utf-8")
    ch = logging.StreamHandler()
    # 日志输出格式,并为handler设置formatter
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 为logger对象添加handler对象,logger对象可以添加多个fh和ch对象
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    f1 = getlogger("alex", "D:/a/ret/c.txt")
    f2 = getlogger("egon", "D:/a/ret/d.txt")
    f1.info("hello")
    f1.info("hello")
    f2.info("ccccc")
    f2.info("ccccc")
