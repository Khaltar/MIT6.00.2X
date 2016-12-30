#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:12:29 2016

@author: jafcpereira
"""

import random
        
def F():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
            
def A():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)
    
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    size = 0
    if songs[0][2] > max_size:
        return []
    song_list = []
    song_list.append(songs[0][0])
    size += songs[0][2]
    songs = sorted(songs, key = lambda tup: tup[2])
    for song in songs:
        if song[0] not in song_list and size + song[2] <= max_size:
            song_list.append(song[0])
            size += song[2]
    return song_list

def resultSum(L,results, s):
    """ input:
            L, list of unique positive integers sorted in descending order
            results, list of results from a greedySum function
            s, positive integer, what the sum should add up to
        return:
            A boolean saying if the sum is the same as s or not
    """
    count_sum = 0
    for i in range(len(L)):
        count_sum += L[i] * results[i]
    if count_sum != s:
        return False
    else:
        return True
        
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    result = []
    multiplier = 1
    size = 0
    biggest = None
    for element in L:
        biggest = 0
        multiplier = 1
        while size + element * (multiplier + 1) < s:
            multiplier += 1
        if size + (element * multiplier) <= s:
            biggest = element * multiplier
            size += biggest
            result.append(multiplier)
        else:
            result.append(0)
    if resultSum(L, result, s):
        return sum(result)
    else:
        return 'no solution'
            
    
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_ending_here = max_so_far = L[0]
    for x in L[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

    
    