import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl  

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data = data.decode()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('Count:',len(results))

sum = 0
for num in results:
    sum += int(num.find('count').text)
    
print(sum)