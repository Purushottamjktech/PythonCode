import json

f = open('data.json','r')

data = json.load(f)

for i in data['employee']:
    print(i)