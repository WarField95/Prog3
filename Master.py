#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:19:25 2019

@author: warfield
"""

from Queue import TaskManager
import time


def __calculate(m, allRuns):
    job_queue, result_queue = m.get_job_queue(), m.get_result_queue()

    in_list = []
    result_list = []
    
    size_task = 10_000
    task_count = int(allRuns/size_task)
    
    for _ in range(task_count):
        in_list.append(size_task)
        
    for i in in_list:
        job_queue.put(i)
        
    job_queue.join()
    
    while not result_queue.empty():
        result_list.append(result_queue.get()) 
    return sum(result_list) / float(len(result_list))

if __name__ == '__main__':
    
    allRuns = 1_000_000
    server_ip = "localhost"
    server_socket = 9999
    TaskManager.register('get_job_queue')
    TaskManager.register('get_result_queue')
    m = TaskManager(address=(server_ip, server_socket), authkey = b'secret')
    m.connect()

    t1 = time.time()
    print("masterIsRunning")
    result = __calculate(m, allRuns)
    t2 = time.time()
    print(' result: ', result)
    print(' time:   ', t2-t1, ' s\n')