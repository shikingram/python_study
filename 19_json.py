import json

data = [{"name":"kingram","age":26},{"name":"anna","age":18}]

# json 转字符串
datastr = json.dumps(data)
print(datastr)

# json转字典
data2 = json.loads(datastr)
print(data2)

"""
[{"name": "kingram", "age": 26}, {"name": "anna", "age": 18}]
[{'name': 'kingram', 'age': 26}, {'name': 'anna', 'age': 18}]
""" 