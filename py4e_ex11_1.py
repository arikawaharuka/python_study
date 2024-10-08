#py py4e_ex11_1.py

import re

#Line-by-Line operation
#fhandle = open('regex_sum_42.txt')
fhandle = open('regex_sum_2071331.txt')
fsum = 0
lst = list()

for line in fhandle:
    line = line.rstrip()
    lst = re.findall('[0-9]+',line)
    if len(lst) == 0:
        continue
    for x in lst:
        x = int(x)
        fsum = fsum + x

print(fsum)


#list comprehension
print(sum([int(x) for x in re.findall('[0-9]+',open('regex_sum_2071331.txt').read())]))