#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Jerry.Shi
# File    : analysis_service.py
# PythonVersion: python3.6
# Date    : 2022/2/15 19:15
# Software: PyCharm


import subprocess
import signal
import os, sys, time
import multiprocessing as mp
from sanic import Sanic
from sanic.response import json as sjson
import asyncio
#TODO: maybe some package of your own service


# init system path
dir_path = os.path.abspath("../")
sys.path.append(dir_path)


# user-defined package
# from service.status import *
from api_tools import *
from utils.log.log_socket_receiver import *
from utils.log.log_socket_sender import *
#TODO: maybe some package of your own service


# create an instance of sanic service
#TODO: set name of your own service
sanic_name = "nlp-techs"  
sanic_app = Sanic(sanic_name)


# init model
socket_sender_logger.info("Service Started! Init model...")
data_path = "../data"
#TODO: Init model here


socket_sender_logger.info("Define some global variables")
# TODO, modified those parameters for service
# num_worker: 
num_worker = 1
service_ip = "172.31.6.84"
service_port = "6006"
service_version = "1.0.1"
service_ip_port = service_ip + ":" + service_port
service_name = "ai-nlp-techs"

logout_dir_path = "../logout"
gunicorn_pid_file_name = "gunicorn_pid_file.txt"
# TODO, file name of the current python 
name_of_this_file = "service"



#TODO: 1) set route path and methods of your own service. 
#         Route path should follow designative rules.
#      2) write the code of your own function
@sanic_app.route('/ai/nlp/test', methods=['POST'])
async def post_process(request):
    ''' process post request which is call for different functions which is judged by function_name in route path

    Returns:
        response: json-like, which contains code(int), message(string),
                  requestId(int), result(string/number/object/array/dict).

    '''
    data = request.json

    socket_sender_logger.info("Request->{}".format(data))
    # Final response result
    response = {
        "code": 0,
        "message": "null",
        "result": "Hello world!"
    }
    response = sjson(response)

    return response


#TODO: If you need timed task, enable this function. Otherwise, remove it.
# define crontab
# async def update_data():
#     while True:
#     	#TODO: modify time interval as you need
#         await asyncio.sleep(300)
#         try:
#             #TODO: write code of your timed task.
            
#         except Exception as e:
#             socket_sender_logger.error("timed task failed, with error: "+str(e))


#TODO: If you need timed task, enable this procedure. Otherwise, remove it.
# using add_task to enable crontab
# sanic_app.add_task(update_data())



def run_app():
    """start sanic application using gunicorn

    """

    print("start to run sanic server!")
    retcode = os.system(
        "gunicorn --workers={} --worker-class sanic.worker.GunicornWorker {}:sanic_app -b {} -t 600".format(num_worker, name_of_this_file, service_ip_port))



def log():
    """ log by socket server

    """

    tcp_server = LogRecordSocketReceiver(log_service_ip, log_service_port)
    print('About to start TCP server...')
    tcp_server.serve_until_stopped()


if __name__ == "__main__":
    # create subprocess
    sanic_process = mp.Process(target=run_app, daemon=False)
    # # register_process = mp.Process(target=register, daemon=False)
    log_process = mp.Process(target=log, daemon=False)

    # # start subprocess
    log_process.start()
    time.sleep(2)
    sanic_process.start()
    #TODO: set sleep time according to start-up time of your own sanic process
    time.sleep(20)

    # save pid of main process，which is used to stop main process
    with open("../logout/{}-main-pid.txt".format(service_name), "w") as f:
        f.write(str(os.getpid()) + "\n")

    # wait for ending of sanic_process
    sanic_process.join()
    
    # stop report heartbeat of service
    if (not sanic_process.is_alive()) and (log_process.is_alive()):
        log_process.terminate()
