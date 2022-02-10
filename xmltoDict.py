import json

from bs4 import BeautifulSoup
import xmltodict
import pprint

with open('pa.xml','r') as rose:
    my_file =rose.read()

my_dict = xmltodict.parse(my_file)

# here our xml file is converted into dict
#now, we convert dict to json file

json_data = json.dumps(my_dict)

with open('pa1.json','w') as json_file:
    json_file.write(json_data)


