import xml.etree.ElementTree as e
import urllib.request as u

url = 'http://py4e-data.dr-chuck.net/comments_151107.xml'

html = u.urlopen(url).read().decode()
tree = e.fromstring(html)

counts = tree.findall('.//count')
count = 0
for i in counts:
    count += int(i.text)
print(count)
