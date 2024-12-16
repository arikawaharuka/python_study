#quiz chapter 6

#question 1
#the role of '+' in string
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

#question 3
#string begin from '0'
x = 'From marquard@uct.ac.za'

#question 4
x = 'From marquard@uct.ac.za'
rpos=x.find('.')
lpos=x.find('@')
print(lpos,rpos)
print(x[lpos+1:rpos])

#question 6
#Method 'len' can calculate the length of string 
print(len('banana')*7)

#question 7
#method upper/lower will copy the string and 
# return a new string with all capital/small
# letters of the string  
greet = 'Hello Bob'
print(greet.upper())

#question 8
#useful of dir()
#print(dir(greet))

#question 9
#[x:y]is the end is up to but not including
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
print('i think that the result will be :.ma')