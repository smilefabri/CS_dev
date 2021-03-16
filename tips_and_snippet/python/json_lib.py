import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(x['cars'])

"""
i can convert: 

dict
list
tuple
string
int
float
True
False
None




"""

y = json.dumps(x)

with open("test.json","w") as outfile:
    json.dump(x,outfile)

