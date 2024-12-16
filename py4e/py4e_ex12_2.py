# py py4e_ex12_2.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lists = list()
ssp = 0

# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    #nlist = re.findall('.+>([0-9]+).+',tag.decode())
    #ssp = ssp + int(nlist[0])
    ssp = int(tag.text) + ssp
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

print(ssp)