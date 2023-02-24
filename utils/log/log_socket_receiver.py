#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Jerry.Shi
# File    : analysis_service.py
# PythonVersion: python3.6
# Date    : 2022/2/15 19:15
# Software: PyCharm

import pickle
import logging
import logging.handlers
import socketserver
import struct


#TODO: Set log_file_name, which should be equal to sanic name
log_file_name = "nlp-techs" 
name = "socket_server"
logger = logging.getLogger(name)
# N.B. EVERY record gets logged. This is because Logger.handle
# is normally called AFTER logger-level filtering. If you want
# to do filtering, do it at the client end to save wasting
# cycles and network bandwidth!
time_file_handler = logging.handlers.TimedRotatingFileHandler("../log/"+log_file_name, when='S', interval=86400, backupCount=30) #86400 = one day
time_file_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
formatter = logging.Formatter(fmt='%(asctime)s\t%(filename)s [line:%(lineno)d] %(levelname)s\t%(message)s', datefmt="%a, %d-%b-%Y %H:%M:%S")
time_file_handler.setFormatter(formatter)
logger.addHandler(time_file_handler)


class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    """Handler for a streaming logging request.

    This basically logs the record using whatever logging policy is
    configured locally.
    """

    def handle(self):
        """
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format. Logs the record
        according to whatever policy is configured locally.
        """

        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            obj = self.unPickle(chunk)
            record = logging.makeLogRecord(obj)
            self.handleLogRecord(record)

    def unPickle(self, data):
        return pickle.loads(data)

    def handleLogRecord(self, record):
        # if a name is specified, we use the named logger rather than the one
        # implied by the record.
        global logger 
        logger.handle(record)


class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
    """
    Simple TCP socket-based logging receiver suitable for testing.
    """

    allow_reuse_address = True

    def __init__(self, host='localhost',
                 port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
                 handler=LogRecordStreamHandler):
        socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.abort = 0
        self.timeout = 1
        self.logname = None

    def serve_until_stopped(self):
        import select
        abort = 0
        while not abort:
            rd, wr, ex = select.select([self.socket.fileno()],
                                       [], [],
                                       self.timeout)
            if rd:
                self.handle_request()
            abort = self.abort

