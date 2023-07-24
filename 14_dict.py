# 字典

my_dict = {}
my_dict2 = dict()
my_dict3 = {"kingram":26,"anna":18}
print(f"字典1的内容是{my_dict},字典2的内容是{my_dict2},字典3的内容是{my_dict3}")
age = my_dict3["kingram"]
print(f"kingram的年龄是{age}")

# 新增
my_dict3["duo"] = 22
print(my_dict3)

# 更新
my_dict3["duo"] = 23
print(my_dict3)

# 删除
my_dict3.pop("duo")
print(my_dict3)

# 清空
my_dict3.clear()
print(my_dict3)

# 获取全部key
my_dict4 = {"kingram":26,"anna":18}
keys = my_dict4.keys()
print(keys)

# 遍历
for x in keys:
    print(f"字段的key是{x},value是{my_dict4[x]}")

for x in my_dict4:
    print(f"字段的key是{x},value是{my_dict4[x]}")
"""
字典1的内容是{},字典2的内容是{},字典3的内容是{'kingram': 26, 'anna': 18}
kingram的年龄是26
{'kingram': 26, 'anna': 18, 'duo': 22}
{'kingram': 26, 'anna': 18, 'duo': 23}
{'kingram': 26, 'anna': 18}
{}
dict_keys(['kingram', 'anna'])
字段的key是kingram,value是26
字段的key是anna,value是18
字段的key是kingram,value是26
字段的key是anna,value是18
"""