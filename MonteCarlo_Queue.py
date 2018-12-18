from Prog3.Blatt9 import MonteCarlo

import multiprocessing
import math
import os
from threading import Thread
import random
import time



timeRand = []

mode = 0

nrOfCores = multiprocessing.cpu_count()
print("nrOfCores: ", nrOfCores)


bruetalshit = 900


def getRandom(self, min=0, max=1000):
    rand = 1
    rand = random.randint(min, max)
    return rand

def getCongruentialRand(self, a, b, m):
    if self.congruentialRand == None:
        self.congruentialRand = int(m / 2) # r_0
    self.congruentialRand = (a * self.congruentialRand + b) % m # r_n++
    return self.congruentialRand

    # Function to check if a random point is inside the circle quarter
def checkIfInside():
    x = 0
    y = 0
    m = 1000
    timeStart = time.clock()

    if mode == 0:
        x = float(getRandom(0, m) / m)
        y = float(getRandom(0, m) / m)
    elif mode == 1:
        '''
        DO NOT CHANGE NUMERS a OR b
        See Table at:
        https://de.wikipedia.org/wiki/Kongruenzgenerator#Verz%C3%B6gerter_Fibonacci-Generator
        '''
        a = 607
        b = 273

        x = float(getCongruentialRand(a, b, m) / m)
        y = float(getCongruentialRand(a, b, m) / m)

    timeRand.append(float(time.clock() - timeStart))

    return math.sqrt(2 * (x * y))

def getPi_MonteCarlo(bruetalshit):
    # init variables
    inside = 0
    all = 0
    totalRuns = 0

    # Run 900 times
    while totalRuns < bruetalshit:
        if checkIfInside() <= 1:
            inside = inside + 1
        all = all + 1
        totalRuns = totalRuns + 1

    # Return approximated pi (1 / 4 of circle)
    return str((inside / all) * 4)


def worker_MonteCarlo(inQ, outQ):
    while True:
        arguments = inQ.get()
        result = getPi_MonteCarlo(*arguments)
        outQ.put(result)
        inQ.task_done()




def main():

    bruetalshit = 90000
    bruetalshitCor = bruetalshit/nrOfCores

    result_queue=multiprocessing.Queue()
    in_queue=multiprocessing.Queue()

    processes = []

    for i in range(nrOfCores):
        p = multiprocessing.Process(target=worker_MonteCarlo, args=(in_queue, result_queue))
        processes.append(p)
        p.start()

    for parameter_set in range(os.cpu_count()):
        in_queue.put(bruetalshitCor)

    in_queue.join()

    result_list = []

    while not result_queue.empty():
        result_list.append(result_queue.get())

        for p in processes:
            p.terminate()

    print(sum(result_list)/len(result_list))



