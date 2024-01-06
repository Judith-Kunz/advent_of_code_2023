# Advent of Code: Door 09


# imports
import regex as re
import math


# functions

def recursive_pyramid(input):
    if all(i==0 for i in input):
        return input+[0]
    
    parent=[]
    i=0
    for i in range(len(input)-1):
        j=i+1
        diff=input[j]-input[i]
        parent.append(diff)
    parent_new=recursive_pyramid(parent)
    val_new=parent_new[-1]+input[-1]
    return input+[val_new]

def recursive_pyramid_backwards(input):
    if all(i==0 for i in input):
        return [0]+input

    parent=[]
    i=0
    for i in range(len(input)-1):
        j=i+1
        diff=input[j]-input[i]
        parent.append(diff)
    parent_new=recursive_pyramid_backwards(parent)
    #val_new=parent_new[0]+input[0]
    val_new=input[0]-parent_new[0]
    return [val_new]+input

def part_one(data):
    sum=0
    for l in data:
        new_l=recursive_pyramid(l)
        sum+=new_l[-1]
    return sum

def part_two(data):
    sum=0
    for l in data:
        new_l=recursive_pyramid_backwards(l)
        sum+=new_l[0]
    return sum


# get data set

file = 'data/door09_sequences.txt'
#file = 'data/door09_test.txt'
with open(file,'r') as f:
    lines = f.read()
    lines= lines.split('\n')
    #lines.pop()
    lines_num=[re.findall(r'(-*\d+)', l) for l in lines]
    lines_num=[[int(x) for x in l] for l in lines_num]


# get solutions

#print(part_one(lines_num))
print(part_two(lines_num))

