# creating a dictionary
a = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
p5r4*rint(a)

# getting all the keys from the dictionary
print(a.keys()) # use list(a.keys()) to display as list

# getting all the values from the dictionary
print(a.values())

# getting all the items from the dictionary as a list of tuples
print(a.items())

# nested dict
b = {
    'fruits': {'apple': '5kg', 'custard apple':'3kg' },
    'vegetables': {'cabbage': '1 pc', 'tomato': '500g'},
    'cereals': {'rice': '1kg', 'wheat': '2kg'},
    }

from pprint import pp
pp(b)

# 
# accessing a value from a dict
print(a['Name'])
print(a['Class'])
# print(a['City']) # KeyError: 'City'

# accessing a value from a dict using get()
print(a.get('Name'))
print(a.get('Class'))
print(a.get('City')) # None
print(a.get('City', 'Not Found')) # default value can be specified
print(a.get('Name', 'Not Found'))

# traversing a dict
# style 1
for key in a:
    print(key, a[key])

# style 2
for key, value in a.items():
    print(key, value)

# only values
for value in a.values():
    print(value)

# only keys
for key in a.keys():
    print(key)