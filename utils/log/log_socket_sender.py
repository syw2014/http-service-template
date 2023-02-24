#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Jerry.Shi
# File    : analysis_service.py
# PythonVersion: python3.6
# Date    : 2022/2/15 19:15
# Software: PyCharm


import logging


# set logging information
#TODO: Set log_service_port, which should be service port plus "0".
#      For example, service port is 1001, than log_service_port should be 10010
log_service_ip = "0.0.0.0"
log_service_port = 60060
socket_sender_logger = logging.getLogger('socket_sender_logger')
socket_sender_logger.setLevel(logging.INFO)
socket_handler = logging.handlers.SocketHandler(log_service_ip, log_service_port)
## don't bother with a formatter, since a socket handler s
## ends the event as an unformatted pickle
socket_sender_logger.addHandler(socket_handler)
