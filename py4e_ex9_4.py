#9.4 Write a program to read through the mbox-short.txt and figure out
#  who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of
#  those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's 
# mail address to a count of the number of times they appear 
# in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
handle = open(name)
#handle = open('mbox-short.txt')
sender = dict()
lists = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    lists = line.split()
    #print(lists[1])
    sender[lists[1]] = sender.get(lists[1],0) + 1
#print(sender)

msender = None
mvalue = None
for key,value in sender.items():
    if mvalue is None or value > mvalue:
        msender = key
        mvalue = value
print(msender,mvalue)

