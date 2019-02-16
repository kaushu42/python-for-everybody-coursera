import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Kaushal</name>
    <phone type="intl">
        +977 123 456 7890
    </phone>
    <email hide="yes"> kaushu42@gmail.com </email>
</person>
'''
tree = ET.fromstring(data)
for i in tree:
    print(i.text.strip())
print(f'Hide Email: {tree.find("email").get("hide")}')
