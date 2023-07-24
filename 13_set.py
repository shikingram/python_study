# set 不支持元素重复

"""
变量名 = set()
"""

my_set = {"kingram","brandon","kingram","anna","duo"}
print(my_set,type(my_set))

# 添加元素
my_set.add("jan")
print(my_set)

# 移除元素
my_set.remove("brandon")
print(my_set)

# 随机取一个
ele = my_set.pop()
print(ele)
print(my_set)

# 清空元素
my_set.clear()
print(my_set)

# 取两个集合的差集 (集合1有  集合2 没有的，得到一个新集合)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print("取差集")
print(set1)
print(set2)
print(set3)

# 消除差集（在集合1 中删除 集合2中有的元素，集合1会发生变化，集合2不变）
set1.difference_update(set2)
print("消除差集")
print(set1)
print(set2)

# 合并两个集合
set4 = set1.union(set2)
print("合并集合")
print(set1)
print(set2)
print(set4)

# 集合的遍历
set5 = {1,2,3,4,5}
i = 0
for x in set5:
    print(x)

"""
{'kingram', 'anna', 'duo', 'brandon'} <class 'set'>
{'brandon', 'anna', 'duo', 'jan', 'kingram'}
{'anna', 'duo', 'jan', 'kingram'}
anna
{'duo', 'jan', 'kingram'}
set()
取差集
{1, 2, 3}
{1, 5, 6}
{2, 3}
消除差集
{2, 3}
{1, 5, 6}
合并集合
{2, 3}
{1, 5, 6}
{1, 2, 3, 5, 6}
1
2
3
4
5
"""