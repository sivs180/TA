user_dict = {}
with open('C:\Users\sindu\Documents\Sinduja Sivakumar\Extra-Curriculars\Computer Science Internship\Data\TAusers.csv', 'r') as f:
    # need to avoid header
    header = next(f)
    # add comment about what loop is doing
    #change value of dictionary from list to set
    for line in f:
        line = line.strip().split(',')
        if line[0] in user_dict:
            user_dict[line[0]].add(line[1])
        else:
            user_dict[line[0]] = {line(1)}

# now file is closed

#list: append, set: add
#new list: [hotel], new set: set(hotel)

# next loop, you iterate through the dictionary (iteritems), and print the value
# for key, value in user_dict.iteritems():
for key, value in user_dict.iteritems():
    print 'The value for', key, user_dict[key]