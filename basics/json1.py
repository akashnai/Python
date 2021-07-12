import json

# x = {"name": "akki", "age": 18, "passion": "coding"}
x = '{"name": "akki", "age": 18, "passion": "coding"}'

# y = json.dumps(x)

y = json.loads(x)

print(y)