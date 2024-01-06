# Advent of Code: Door 05


# imports
import regex as re
import numpy as np


#functions

def get_location(input):
    for seed_pair in input:
        for seed in range(seed_pair[0],seed_pair[1],1):
            #current_value
            value=seed
            for map in mappings:
                for i in all_map[map]:
                    lower_boundary=int(i[1])
                    upper_boundary=int(i[1])+int(i[2])
                    if lower_boundary<=int(value)<upper_boundary:
                        diff=int(value)-int(i[1])
                        value=int(i[0])+diff
                        break
                    else:
                        continue
            
            locations.append(value)

    return(min(locations))


# get data set
file = 'data/door05_mapping.txt'
#file = 'data/door05_test.txt'
with open(file,'r') as f:
    lines = f.read()
    lines= [l.split('\n') for l in lines.split('\n\n')]


seeds_str=lines[0][0].partition(':')[2]
seeds_pairs=re.findall('(\d+\s\d+)',seeds_str)
seeds=[]
for s in seeds_pairs:
    s=s.split(' ')
    s_temp=[int(s[0]),int(s[0])+int(s[1])-1]
    s=s_temp
    seeds.append(s)

all_map={}

for i in range(1,len(lines)):
    name_map=lines[i][0].strip(' map:')
    mapping=[[int(e) for e in l.split(' ')] for l in lines[i][1:]]
    all_map[name_map]=mapping

mappings=all_map.keys()
locations=[]


inputs=seeds

for step in mappings:
    new_inps=[]
    converted=[]
    leftover=[]
    for inp in inputs:
        been_mapped=False
        for m in all_map[step]:
            if ((m[1]>inp[1]) or (m[1]+m[2]-1<inp[0])):
                    continue
            else:
                # start mapping
                
                #CASE 1
                # if input range falls within borders of mapping range
                # also if either or both of input borders are equal to mapping borders (start-start,end-end)
                if inp[0]>=m[1] and inp[1]<=m[1]+m[2]-1:
                    diff1=inp[0]-m[1]
                    diff2=inp[1]-inp[0]
                    inp_new=[m[0]+diff1,m[0]+diff1+diff2]
                    new_inps.append(inp_new)
                    converted.append(inp)
                    been_mapped=True
                #CASE 2
                # if input start lies outside mapping range, but input end lies within
                elif inp[0]<m[1] and inp[1]<=m[1]+m[2]-1:
                    inp_new1=[inp[0], m[1]-1]
                    diff=inp[1]-m[1]
                    inp_new2=[m[0],m[0]+diff]
                    new_inps.append(inp_new2)
                    converted.append([m[1],inp[1]])
                    leftover.append(inp_new1)
                    been_mapped=True
                #CASE 3
                # if input lies within mapping range, but input end does not
                elif inp[0]>=m[1] and inp[1]>m[1]+m[2]-1:
                    inp_new1=[m[1]+m[2],inp[1]]
                    diff=inp[0]-m[1]
                    inp_new2=[m[0]+diff,m[0]+m[2]-1]
                    new_inps.append(inp_new2)
                    converted.append([inp[0],m[1]+m[2]-1])
                    leftover.append(inp_new1)
                    been_mapped=True
                #CASE 4
                # if mapping range falls within borders of input range
                elif inp[0]<m[1] and inp[1]>m[1]+m[2]-1:
                    inp_new1=[inp[0],m[1]-1]
                    inp_new2=[m[1]+m[2],inp[1]]
                    inp_new3=[m[0],m[0]+m[2]-1]
                    leftover.extend((inp_new1,inp_new2))
                    converted.append([m[1],m[1]+m[2]-1])
                    new_inps.append(inp_new3)
                    been_mapped=True
                #CASE X
                # how did we end up here?
                else:
                    print("ERROR")
                    print(step)
                    print(inp)
                    print(m)
                    break
        # back to inp level
        if not been_mapped:
            new_inps.append(inp)

    
    converted=sorted(converted, key=lambda x: x[0])
    i=0
    while i<=len(converted)-2:
        j=i+1
        if converted[j][0]-converted[i][1]==1:
           converted[i]=[converted[i][0],converted[j][1]]
        else:
            i+=1

    leftover_checked=[]
    for l in leftover:
        is_c=False
        is_partial_c=False
        for c in converted:
            if l[0]>c[1] or l[1]<c[0]:
                continue
            elif l[0]>=c[0] and l[1]<=c[1]:
                is_c=True
                break
            elif l[0]>=c[0] and l[1]>c[1]:
                leftover_checked.append([c[1]+1,l[1]])
                is_partial_c=True
            elif l[0]<c[0] and l[1]<=c[1]:
                leftover_checked.append([l[0],c[0]-1])
                is_partial_c=True
            else:
                print("error")
                print(l)
                print(c)
                break
        if not is_partial_c and not is_c:
            leftover_checked.append(l)
        if is_c:
            break

    inputs=new_inps+leftover_checked
    inputs_unique = np.unique(np.array(inputs), axis=0)
    inputs_unique = inputs_unique.tolist()
    inputs=inputs_unique

minimum=min(inputs, key=lambda x: x[0])
print(minimum[0])

