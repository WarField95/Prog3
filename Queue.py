#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:19:21 2019

@author: warfield
"""

from multiprocessing.managers import BaseManager
from multiprocessing import JoinableQueue, Queue

class TaskManager(BaseManager):
    pass

if __name__ == "__main__":
    masterSocket = 9999
    taskQueue = JoinableQueue()
    resultQueue = Queue()
    TaskManager.register("get_job_queue", callable = lambda: taskQueue)
    TaskManager.register("get_result_queue", callable = lambda: resultQueue)
    m = TaskManager(address = ("", masterSocket), authkey = b"secret")
    
    print("starting queue server, socket", masterSocket)
    m.get_server().serve_forever()
