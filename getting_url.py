import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
list = []
url = input('Enter URL - ')

while count < 7 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags :
        URL = tag.get('href', None)
        list.append(URL)
    url = list[17]
    count += 1
    list.clear()

print(url)
