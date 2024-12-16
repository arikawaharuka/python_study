#10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of 
# the messages. You can pull the hour out from the 'From ' line 
# by finding the time and then splitting the string a second time 
# using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

#py py4e_ex10_2.py

name = input("Enter file:")
#name = "mbox-short.txt"
handle = open(name)
hdic = dict()
hlist = list()
slist = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    hlist = line.split()
    tstr = hlist[5]
    hour = tstr[:2]
    hdic[hour] = hdic.get(hour,0) + 1
slist = sorted(hdic.items())
for k,v in slist:
    print(k,v)
