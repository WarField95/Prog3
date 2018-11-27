import random
import math



def rollDice():
    roll = float(random.randint(0, 1000) / 1000)
    return roll

def RandomPoint():
    return([rollDice(), rollDice()])

def Calc(ortsvector):
    return math.sqrt(2 * (ortsvector[0] * ortsvector[1]))
##root < 1 so squareroot <1, math hits in your face


# def seed(x):
#     global xi
#     xi=x
#
# def rng(a, c, m):
#     global xi
#     xi=(a*xi+c)%m
#     return xi

def congruentialGenerator(self, a, b, m):
    rand = m - a
    for i in range(m):
        rand = (a * rand + b) % m

    return rand


def MonteCarlo(innen, alle, runs, min, max):
    runs = runs + 1
#    randomP = RandomPoint()
    randomP=congruentialGenerator(min, random.randint(min,max), max)
    if Calc(randomP) <= 1:
        innen = innen + 1
    alle = alle + 1
    while runs < 900:
        return MonteCarlo(innen, alle, runs)
    else:
        return (innen / alle) * 4


def main():
    a=2
    c=9
    m=16
    xi=0
    print (MonteCarlo(0,0,0,0,1000))


