# Advent of Code: Door 02


# imports
import regex as re
import numpy as np


# functions

def get_drawings(pattern,s):
    return re.findall(pattern,s)

def get_tuple(s):
    key=re.search('[a-zA-Z]+',s).group()
    count=int(re.search('\d+',s).group())
    return (key,count)

def part_one(input,test):
    sum=0
    for line in input:
        line_id=int(re.search(r'\d+',line).group())
        drawings=get_drawings(r'\d+ red|\d+ green|\d+ blue',line)
        i=0
        flag=True
        while (i<len(drawings)) and (flag):
            tup=get_tuple(drawings[i])
            if test[tup[0]]>=tup[1]:
                pass
            else:
                flag=False
                break
            i+=1
        if flag:
            sum=sum+line_id
        else:
            pass
    return(sum)

def part_two(input):
    sum=0
    for line in input:
        drawings=get_drawings(r'\d+ red|\d+ green|\d+ blue',line)
        max_count={'red':0,'green':0,'blue':0}
        i=0
        while i<len(drawings):
            tup=get_tuple(drawings[i])
            if max_count[tup[0]]<tup[1]:
                max_count.update({tup[0]: tup[1]})
            else:
                pass
            i+=1
        product=np.prod(list(max_count.values()))
        sum=sum+product
    return(sum)


# select data set

#data = open('data/door02_test.txt','r')
data = open('data/door02_games.txt','r')
lines = data.readlines()


# get solution 

test={'red':12,'green':13,'blue':14}
print(part_one(lines,test))
print(part_two(lines)) 



    
    
