#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Jerry.Shi
# File    : analysis_service.py
# PythonVersion: python3.6
# Date    : 2022/2/15 19:15
# Software: PyCharm

import json
from utils.status.status import *
from utils.log.log_socket_sender import *


def post_request(request, func, func_name, *args):
    """
    :param func: 
    :return: post_data: post data
             post_result: 
    """
    # 用户发出请求不存在
    if not request.json:
        return None, None, 21102, E_MSG[21102]
    # 获取POST传递的form格式参数
    post_data = request.form
    parameters = {}
    for param in args:
        # 用户发出请求有误
        if param not in post_data:
            return None, None, 21101, E_MSG[21101]
        parameters[param] = post_data[param][0]
    # 将字典格式的post_data，传给调用的功能函数作为参数
    try:
        #print(parameters)
        post_result = func(**parameters)
    # 捕获应用代码的内部逻辑异常
    except Exception as e:
        code = function_error_code_dict[func_name]
        socket_sender_logger.error("Call function: {}, failed with error: {}".format(func_name, str(e)))
        return None, None, code, E_MSG[code]
    return post_data, post_result, 0, E_MSG[0]
