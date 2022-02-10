import json


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as rose:
        file_data = json.load(rose)

        file_data["employee"].append(new_data)

        rose.seek(0)

        json.dump(file_data,rose, indent=4)

p = {
            "id": "06",
            "name": "purushottam",
            "department": "development"
     }
write_json(p)
