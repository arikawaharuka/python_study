# Exercise 5: This program records the domain name 
# (instead of the address) where the message was sent from instead of 
# who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary
# Sample Execution:
# >>> python schoolcount.py
# >>> Enter a file name: mbox-short.txt
# >> {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# >> 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = input("Enter file:")
#fhandle = open(fname)
fhandle = open('mbox-short.txt')
domain = dict()
dlist = list()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    dlist = line.split()
    address = dlist[1]
    dpos = address.find('@')
    dname = address[dpos+1:len(address)]
    domain[dname] = domain.get(dname, 0) + 1
print(domain)
