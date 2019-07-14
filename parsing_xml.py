#  Parsing XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sumsum = 0
url = input('url: ')

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
decoded_data = data.decode()
tamtam = ET.fromstring(decoded_data)
lst = tamtam.findall('comments/comment')
print('num: ', len(lst))

for item in lst :
     #  print(item.find('count').text)
     decoded_data = item.find('count').text
     sumsum = sumsum + int(decoded_data)

print(sumsum)
