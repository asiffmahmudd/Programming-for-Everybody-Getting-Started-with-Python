import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Url:')
print('Retrieving data from', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)
print('Retrieved', len(str(info)), 'characters')

sum = 0
for num in info['comments']:
    sum += int(num['count'])
print(len(info['comments']))
print(sum)