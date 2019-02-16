import urllib.request as ureq
import re
f = ureq.urlopen('https://www.coursera.org')
#f = ureq.urlopen('http://data.pr4e.org/romeo.txt')

text = f.read()
[print(f'{i}\n\n') for i in re.findall(r'<h1 .+>.*</h1>', text.decode())]
