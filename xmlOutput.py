import xmltodict
import pprint

# in this program we are converting the xml file to Dict.

with open('pa.xml','r') as rose:
    my_file =rose.read()

my_dict = xmltodict.parse(my_file)

pprint.pprint(my_dict,indent=3)
#print(my_dict)

