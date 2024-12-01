import numpy as np


# load file
list1 = []
list2 = []
with open('input.txt', 'rt') as f:
    for line in f:
        split_line = line.split()
        print(split_line)
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))

count_dict = {}

# build a dictionary with ID:number of occurences mapping
for num in list2:
    try:
        count = count_dict[num]
        count_dict[num] =  count + 1
    except KeyError:
        count_dict[num] = 1

similarity_score = 0

for num in list1:
    try:
        count = count_dict[num]
    except KeyError:
        count = 0
    similarity_score += num*count

print('similarity score: ', similarity_score)
