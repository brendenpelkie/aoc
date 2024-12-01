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


# compute distances and sum

distances = np.abs(np.sort(np.array(list1)) - np.sort(np.array(list2)))
total = np.sum(distances)

print(total)
