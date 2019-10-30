# some JSON:
import json
with open('example2.txt') as json_file:
    x = json.load(json_file)

# with open('example.json') as json_file:
#     x = json.loads(json_file)



# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"]["first"])
