#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:19:23 2019

@author: warfield
"""

from Queue import TaskManager
import multiprocessing
import itertools
import random, math



def monteCarlo(allRuns = 900):
    m = 1000
    resultInside = 0
    
    for i in range(0, allRuns):
        if(math.sqrt(2 * (float(random.randint(0, m) / m) * float(random.randint(0, m) / m)))) <= 1:
            resultInside += 1
            
    return (resultInside / allRuns) * 4

#
#def queueLoop(inQ, outQ):
#    while True:
#        arguments = inQ.get()
#        py = monteCarlo(arguments)
#        outQ.put(py)
#        inQ.task_done()
#        
#        
#def monteCarloParallelQueue(allRuns = 900):
#    nrOfCores = multiprocessing.cpu_count()
#    inQueue = multiprocessing.JoinableQueue()
#    resultQueue = multiprocessing.Queue()
#    
#    
#    processes = []
#    
#    for i in range(nrOfCores):
#        p = multiprocessing.Process(target = queueLoop, args = (inQueue, resultQueue))
#        
#        processes.append(p)
#        p.start()
#        
#        
#    for param_set in range(nrOfCores):
#        inQueue.put(int(allRuns/4))
#        
#        inQueue.join()
#        
#        resultList = []
#        
#    while not resultQueue.empty():
#        resultList.append(resultQueue.get())
#        
#    for p in processes:
#        p.terminate()
#        
#    resultInside = 0
#    
#    res = sum(resultList) / len(resultList)
#
#    return (res)
#  
#def main():
#    runsTotal=100
#    
#    print(monteCarlo(runsTotal))
#    print(monteCarloParallelQueue(runsTotal))
    
def __worker_function(job_queue, result_queue):
    while True:
        task = job_queue.get()
        result = monteCarlo(task)
        result_queue.put(result)
        job_queue.task_done()

def __start_workers(m):
    job_queue, result_queue = m.get_job_queue(), m.get_result_queue()
    nr_of_processes = multiprocessing.cpu_count()
    processes = [multiprocessing.Process(target = __worker_function,
            args = (job_queue, result_queue))
        for i in range(nr_of_processes)]
    for p in processes:
        p.start()
    return nr_of_processes

if __name__ == '__main__':
    server_ip = "localhost"
    server_socket = 9999
    TaskManager.register('get_job_queue')
    TaskManager.register('get_result_queue')
    m = TaskManager(address=(server_ip, server_socket), authkey = b'secret')
    m.connect()
    
    nr_of_processes = __start_workers(m)
    print(nr_of_processes, 'workers started')
