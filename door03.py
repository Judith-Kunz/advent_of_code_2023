# Advent of Code: Door 03


'''
Principal concept: distance functions

euclidean dist: if dist>2 pass, else stay
compare distances between numbers and symbols, if distance i too great, break
Disclaimer: Only works if numbers have no more than three digits!
'''


# imports

import numpy as np
import regex as re
from scipy.spatial.distance import pdist


# functions

def prep(input,count=0):
    loc_nums=[]
    loc_sign=[]
    for line in input:
        m=re.finditer(r'\d+',line)
        row=[]
        for match in m:
            col=[match.group(),match.span()]
            row.append(col)
        if len(row)>0:
            row.insert(0,count)
            loc_nums.append(row)

        s=re.finditer(r'[^\.\d\n]',line)
        row_s=[]
        for match in s:
            col=[match.group(),match.span()]
            row_s.append(col)
        row_s.insert(0,count)
        loc_sign.append(row_s)
        count+=1
    return loc_nums,loc_sign

def part_one(loc_nums,loc_sign,num_rows,engine=0):
    for l in loc_nums:
        r=l[0]
        for elem in l[1:]:
            engine_flag=False
            for i in range(max(0,l[0]-1),min(l[0]+2,num_rows)):
                len_arr=len(loc_sign[i])
                if len_arr==1:
                    continue
                else:
                    for sign in loc_sign[i][1:]:
                        number_min=elem[1][0]
                        number_max=(elem[1][1])-1
                        sign=sign[1][0]
                        c1=pdist([[number_min,r],[sign,i]])
                        c2=pdist([[number_max,r],[sign,i]])
                        if (c1<2 or c2<2):
                            engine_flag=True
                        else:
                            pass
            if engine_flag:
                engine+=int(elem[0]) 
    return engine

def part_two(input):
    i=0
    sum=0
    while i<len(input):
        line=input[i]
        stars=[x for x in re.finditer(r'\*',line)]
        if len(stars)<1:
            i+=1
            continue
        previous=input[max(0,i-1)]
        previous_nums=[x for x in re.finditer(r'\d+',previous)]
        following=input[min(i+1,len(input)-1)]
        following_nums=[x for x in re.finditer(r'\d+',following)]
        if i in range(1,len(input)-1):
            current_nums=[x for x in re.finditer(r'\d+',line)]
            pot_mat=previous_nums+current_nums+following_nums
        else:
            pot_mat=previous_nums+following_nums
        for star in stars:
            num_counter=0
            nums=[]
            ps=star.span()[0]
            for m in pot_mat:
                pm1=m.span()[0]
                pm2=m.span()[1]-1
                if (abs(ps-pm1)<=1 or abs(ps-pm2)<=1):
                    nums.append(int(m.group()))
                    num_counter+=1
                    if num_counter>2:
                        break
            if num_counter==2:
                product=np.prod(nums)
                sum+=product

        i+=1
    return sum



# get data set

#data=open('data/door03_test.txt','r')
data = open('data/door03_partnumbers.txt','r')
lines = data.readlines()
num_rows=len(lines)


# get solutions

numbers,signs=prep(lines)
print(part_one(numbers,signs,num_rows))
print(part_two(lines))



