#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:05:17 2016

@author: jafcpereira
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    balls_of_same_color = 0
    for i in range(numTrials):
        balls = ['red', 'green', 'red','green','red','green','red','green']
        drawn_balls = random.sample(balls, 3)
        if drawn_balls == ['red','red','red'] or drawn_balls == ['green','green','green']:
            balls_of_same_color += 1
    return balls_of_same_color / numTrials

        
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title == None:
        pylab.hist(values, bins = numBins)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
    else:
        pylab.hist(values, bins = numBins)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def longest_run(lst):
    from collections import defaultdict
    longest_runs = defaultdict(int)
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            longest_runs[lst[i]] += 1
    for key in longest_runs:
        longest_runs[key] += 1
    try:    
        return max(longest_runs.values())
    except:
        return 1

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_runs = []
    for i in range(numTrials):
        rolls = []
        for j in range(numRolls):
            rolls.append(die.roll())
        longest_runs.append(longest_run(rolls))
    makeHistogram(longest_runs, 10, 'Number Roll', 'Counts')
    return sum(longest_runs) / len(longest_runs)
            
    
    
# One test case
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 6, 10))

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def find_combination(choices, total):
    """
    choices: a non-empty numpy.array of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import numpy as np
    combinations_possible = [combination for combination in subset_sum(choices, total)]
    result_arrays = []
    if len(combinations_possible) != 0:
        for array in combinations_possible:
            result = []
            for element in choices:
                if element in array:
                    result.append(1)
                else:
                    result.append(0)
            result_arrays.append(result)
    else:
        max_result = 0
        for element in choices:
            if max_result + element <= total:
                max_result += element
                result_arrays.append(1)
            else:
                result_arrays.append(0)
        result_arrays = [result_arrays]
    final_array = None
    for array in result_arrays:
        if final_array is None or sum(array) < sum(final_array):
            final_array = array
    return np.array(final_array)
        
    
    
    
    
    
    
        
    
    
