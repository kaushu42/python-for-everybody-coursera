import xml.etree.ElementTree as e

data = '''
<system>
    <users>
        <user id="1">
            <name>Mr. X</name>
            <country visible="true">X</country>
        </user>
        <user id="2">
            <name>Mr. Y</name>
            <country visible="false">Y</country>
        </user>
        <user id="3">
            <name>Mr. Z</name>
            <country visible="true">Z</country>
        </user>
    </users>
    <admins>
        <admin id="1">
            <name>Admin X</name>
            <country visible="false">AX</country>
        </admin>
        <admin id="2">
            <name>Admin Y</name>
            <country visible="false">AY</country>
        </admin>
    </admins>
</system>
'''

tree = e.fromstring(data)
users = tree.findall("users/user")
admins = tree.findall("admins/admin")
print(f"    -Total Users: {len(users)}")
print(f"    -Total Admins: {len(users)}")
print(f'-----USERS-----')

for i in users:
    print('Name: ', i.find('name').text)
    print('Country: ', i.find('country').text)
    print("Country Visible: ", i.find('country').get('visible'))
print('-----ADMINS-----')

for i in admins:
    print('Name: ', i.find('name').text)
    print('Country: ', i.find('country').text)
    print("Country Visible: ", i.find('country').get('visible'))
