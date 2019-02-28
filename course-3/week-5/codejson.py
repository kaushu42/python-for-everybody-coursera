import json

data = '''
[
    {
        "id" : "001",
        "name" : "Mr. A",
    } ,
    {
        "id" : "002",
        "name" : "Mr. B",
    }
]
'''

info = json.loads(data)
print(f'Total Users: {len(info)}')

for i in info:
    print(f'Name: {i.name}')
