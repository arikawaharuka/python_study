import json
import urllib.request

csurl = input('Enter location: ')
print('Retrieving',csurl)
uh = urllib.request.urlopen(csurl)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
sum = 0

for item in info['comments']:
    sum = sum + item['count']
print('Count:',len(info['comments']))
print('Sum:',sum)