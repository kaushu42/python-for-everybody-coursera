import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42 
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params = {}
params['key'] = api_key

while True:
    address = input('Enter Location: ')
    if len(address) < 1: break

    params['address'] = address
    url = serviceurl + urllib.parse.urlencode(params)

    reply = urllib.request.urlopen(url, context=ctx).read().decode()

    try:
        js = json.loads(reply)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Error occured!')
        print(reply)
        continue

    print(js['results'][0]['place_id'])

