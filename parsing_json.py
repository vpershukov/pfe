#  Parsing JSON

import urllib.request, urllib.parse, urllib.error
import ssl
import json


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
url = input('url: ')

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
lst = info['comments']

for i in lst :
    k = i['count']
    sum += k

print(sum)
