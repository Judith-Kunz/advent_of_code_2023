# Advent of Code: Door 08


# imports
import regex as re


# functions

def part_one(input):
    node='AAA'
    i=0
    counter=0
    while node != 'ZZZ':
        next_node=input[node][steps[i]]
        counter+=1
        node=next_node
        if i < len(steps)-1:
            i+=1
        else:
            i=0
    return counter

def part_two(input, step):
    nodes=[s for s in input.keys() if s[2]=='A']
    i=0
    counter=0
    end=False
    while not end:
        next_nodes=[input[node][step[i]] for node in nodes]
        counter+=1
        nodes=next_nodes
        check=[True if node[2]=='Z' else False for node in nodes]
        if all(check):
            end=True
        else:
            if i < len(step)-1:
                i+=1
            else:
                i=0
    return counter


# get data set & preparation

file = 'data/door08_nodes.txt'
#file = 'data/door08_test.txt'
#file = 'data/door08_test2.txt'
with open(file,'r') as f:
    lines = f.read()
    lines= [l.split('\n') for l in lines.split('\n\n')]
steps=lines[0][0]
directions=lines[1]
orders={}
for i in range(0,len(directions)):
    matches=re.findall(r'\w{3}',directions[i])
    if matches:
        orders[matches[0]]={'L': matches[1],'R':matches[2]}


# get solutions

print(part_one(orders))
print(part_two(orders,steps))

