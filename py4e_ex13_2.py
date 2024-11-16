import urllib.request,urllib.parse
import json, ssl

servurl = 'http://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode - ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    address = address.strip()
    parms=dict()
    parms['q'] = address
    url = servurl+urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'features' not in js:
        print('Download Error')
        print(data)
        break
    if len(js['features']) == 0:
        print('Not Found')
        print(data)
        break
    pcode=js['features'][0]['properties']['plus_code']
    print(pcode)
