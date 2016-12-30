#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:12:28 2016

@author: jafcpereira
"""

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])
    
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + ' ' + str(rollDie())
    print(result)
    


def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice([x for x in range(0,100) if x % 2 == 0])
    
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    lst = [x for x in range(9, 22) if x % 2 == 0]
    return lst[2]

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    lst = [x for x in range(9, 22) if x % 2 == 0]
    return random.choice(lst)
    
def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability=',
          round(1/(6**len(goal)), 8))
    estProbability = round(total / numTrials, 8)
    print('Estimated Probability =',
          round(estProbability, 8))
    
runSim('11111', 1000)
runSim('11111', 1000)
    
