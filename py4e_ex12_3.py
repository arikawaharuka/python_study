import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')


count = input('Enter count: ')
pos = input('Enter position: ')

nl = ''
#first name
fst = re.findall('^h.+by_([a-zA-Z].+).html',url)
nl = nl + fst[0] + ' '

# Retrieve all of the anchor tags
for x in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    rc = 1
    for tag in tags:
        if(rc > int(pos)):
            break
        url = tag.get('href', None)
        print(url)
        if(rc == int(pos)):
            nl = nl + tag.text + ' '
        rc = rc + 1
print(nl)

