import json

var = {
    "subjects": {
        "science": 85,
        "physics": 90

    }
}
with open("arraySample.json","w") as p:
    json.dump(var,p)
