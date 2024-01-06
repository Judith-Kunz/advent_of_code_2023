# Advent of Code: Door 01

# imports

import regex as re


# functions

def extract_num(input,string_lst,string_dict):
    pattern=r'(\d|'+'|'.join(string_lst)+r')'
    nums=re.findall(pattern, input,overlapped=True)
    nums_num=[string_dict[x] if x in string_lst else x for x in nums]
    if len(nums_num)==1:
        target_str="".join([nums_num[0],nums_num[0]])
    elif len(nums_num)>1:
        target_str="".join([nums_num[0],nums_num[-1]])
    else:
        print("Error: Length=0")
        return
    target_num=int(target_str)
    return target_num


# select data set

data = open('data/door01_coordinates.txt','r')
#data = open('data/door01_test.txt','r')


# get solution

lines = data.readlines()
digits_dict={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
digits_str=list(digits_dict.keys())
sum=0
for line in lines:
    t=extract_num(line,digits_str,digits_dict)
    sum=sum+t
print(sum)


