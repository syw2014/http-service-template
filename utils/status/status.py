#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Jerry.Shi
# File    : analysis_service.py
# PythonVersion: python3.6
# Date    : 2022/2/15 19:15
# Software: PyCharm

# User define code
#TODO: set error code of your own service. 
E_MSG = {
    0: None,
    21100: 'Input Data is Null',
    21101: 'Input Data lacks parameter',
    21102: 'Input Request does not exist',
    21103: 'Required function does not exist',
    #201200: 'Encoding Format is Not UTF-8',
    40000: 'Word Segment Program Error',
    40010: 'Word Vector Program Error',
    40020: 'NER Program Error',
    40100: 'Keyword Extraction Program Error',
    40110: 'Text Classification Program Error'
}


# 创建一个异常类，程序可以自定义异常信息
class CustomFlaskError(Exception):
    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self, return_code=None, status_code=None):
        Exception.__init__(self)   # Exception类的初始化
        self.return_code = return_code
        self.status_code = status_code

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict()
        # 增加 dict key: return code
        rv['code'] = self.return_code
        # 增加 dict key: message, 具体内容由常量定义文件中通过 return_code 转化而来
        rv['msg'] = E_MSG[self.return_code]
        # 日志打印
        # logger.warning(self.J_MSG[self.return_code])
        return rv
