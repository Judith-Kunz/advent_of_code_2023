# Advent of Code: Door 06


# imports

import regex
import numpy as np
from sympy import *
import math


# get data set

file = 'data/door06_times.txt'
#file = 'data/door06_test.txt'
with open(file,'r') as f:
    lines = f.read()
    lines= lines.split('\n')
    times=regex.findall(r'\d+',lines[0])
    distances=regex.findall(r'\d+',lines[1])


# optimization issue
# distance=speed*time_run
# speed=time_pressed=time_limit-time_run
# distance=(time_limit-time_run)*time_run

# x: time_run
# y: distance
# a: parameter time_limit

x = Symbol('x', real=True)
a=0
record=0


# functions
def dist(x,a):
    return (a-x)*x

def dist2(x,a,r):
    return (a-x)*x-r

def win_this_race(a,record):
    counter=0
    for s in range(0,record):
        if dist(s,a)>record:
            counter+=1
    return counter

def win_this_race2(a,record):
    margins=solve(dist2(x,a,record),x)
    margins=[math.ceil(m) for m in margins]
    return margins[1]-margins[0]


def part_one(t_lst,dist_lst):
    product=1
    for i in range(len(t_lst)):
        c=win_this_race(int(t_lst[i]),int(dist_lst[i]))
        product=product*c
    return product

def part_two():
    with open(file,'r') as f:
        lines = f.read()
        lines= lines.split('\n')
        time=''.join(regex.findall(r'\d+',lines[0]))
        distance=''.join(regex.findall(r'\d+',lines[1]))

    return win_this_race2(int(time),int(distance))


# get solutions

print(part_one(times,distances))
print(part_two())
