# Advent of Code: Door 04


# imports

import regex as re


# functions

def get_matches(s):
    s=re.sub(r'^Card\s+\d+:', '', s)
    s=s.rpartition('|')
    nums_winning=re.findall('\d+',s[0])
    nums_sc=re.findall('\d+',s[2])
    return list(set(nums_winning).intersection(nums_sc))

def part_one(input):
    sum=0
    counter=0
    for line in input:
        matches=get_matches(line)
        if matches:
            points=pow(2,len(matches)-1)
            sum+=points
        counter+=1
    return sum

def part_two(input):
    arr=[]
    count=0
    for line in input:
        if arr:
            arr[0]=arr[0]+1
        else:
            arr=[1]
        count+=arr[0]
        m=len(get_matches(line))
        temp_arr=arr[1:]
        l_temp=len(temp_arr)
        add=arr[0]
        for i in range(m):
            if i>=l_temp:
                temp_arr.append(add)
            else:
                temp_arr[i]=temp_arr[i]+add
        arr=temp_arr
    return count


# get data set

file = 'data/door04_cards.txt'
#file = 'data/door04_test.txt'
with open(file,'r') as f:
    lines = f.read().splitlines() 


# get solutions 

#res=part_one(lines)
#print(res)
print(part_two(lines))