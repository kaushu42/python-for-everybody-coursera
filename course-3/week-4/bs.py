from bs4 import BeautifulSoup
import urllib.request as u

url = 'https://coursera.org'
html = u.urlopen(url).read().decode()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('h1')
for tag in tags:
    print(tag.get('class', None))
