#py py4e_ex11_2.py
#This question is Exercise 11.2 in the textbook

import re
fname = input('Enter file:')
lst = list()

#list comprehension
lst = [int(x) for x in re.findall('N.+: ([0-9]+)',open(fname).read())]
print(sum(lst)/len(lst))

#regular method
fhandle = open(fname)
fsum = 0
count = 0
lists = list()
for line in fhandle:
    line = line.rstrip()
    lists = re.findall('^N.+: ([0-9]+)',line)
    if len(lists) == 0:
        continue
    count = count + 1
    fsum = fsum + int(lists[0])
print(fsum/count)