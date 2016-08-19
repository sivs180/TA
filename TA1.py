import numpy as np


user_dict = {}
with open("Data/subset.txt", 'r') as f:
    # need to avoid header
    header = next(f)
    # add comment about what loop is doing
    # change value of dictionary from list to set
    for line in f:
        line = line.strip().split(',')
        if not line[0]:
            continue
        if line[0] in user_dict:
            user_dict[line[0]].add(line[1])
        else:
            user_dict[line[0]] = {line[1]}

# now file is closed
# list: append, set: add
# new list: [hotel], new set: set(hotel)
# next loop, you iterate through the dictionary (iteritems), and print the value
# for key, value in user_dict.iteritems():
# make matrix in numpy
# matrix = [[None*size]*size]- might have to use to adjust size of matrix
# i = 0- may need to be used for the matrix in outer for loop
# j = 0- may need to be used for the matrix in the inner for loop
# s = (len(user_dict), len(user_dict))
# array = np.zeros(s, dtype=np.int)
# i = 0
# j = 0
adjacency_list = {}
for user1, hotel_list1 in user_dict.iteritems():
    temp = []
    for user2, hotel_list2 in user_dict.iteritems():
        dist = len(hotel_list1 and hotel_list2)
        if dist > 1 and user1 != user2:
            temp.append((user2, dist))
        # print dist
    #     array[i, j] = dist
    #     j += 1
    # i += 1
    if temp:
        adjacency_list[user1] = temp
        # print adjacency_list[user1]
print adjacency_list
print len(user_dict) - len(adjacency_list)
# only want connections that are greater than 1 and if any user doesnt have any connections greater than 1 drop them.

