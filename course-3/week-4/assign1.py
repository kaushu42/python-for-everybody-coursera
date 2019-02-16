import urllib.request as u
from bs4 import BeautifulSoup as BS

url = 'http://py5e-data.dr-chuck.net/comments_151105.html' 
html = u.urlopen(url).read().decode()
soup = BS(html, 'html.parser')
tags = soup('span')

total = sum([int(i.contents[0]) for i in tags])
print(total)

