import json

a = {"name":"purushottam","age":31,"salary":25000}

b= json.dumps(a)
print(b)
print(type(b))