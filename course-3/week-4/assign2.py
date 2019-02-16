import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Lilliarna.html' 
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for i in range(7):
	url = tags[17].get('href', None)
	html = urllib.request.urlopen(url, context=ctx).read().decode()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
print(url)