from bs4 import BeautifulSoup

with open('pa.xml', 'r') as r:
    data = r.read()

print(data)

bs_data = BeautifulSoup(data,'xml')

for tag in bs_data.find_all('Product', {'name':'TV'}):tag["price"]="Hello!!!"

# Output the contents of the
# modified xml file
print(bs_data.prettify())