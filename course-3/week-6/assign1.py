import urllib.request as u
import json

url = 'http://py4e-data.dr-chuck.net/comments_151108.json'
reply = u.urlopen(url)
json_reply = reply.read().decode()
json_reply = json.loads(json_reply)

count = 0
for i in json_reply['comments']:
    count += i['count']
print(count)
