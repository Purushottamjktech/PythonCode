import json

dict = {
    "id":"01",
    "name":"purushottam",
    "company":"jktech"
}

with open("data.json","a") as nolan:
    json.dump(dict,nolan)