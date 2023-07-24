# 列表定义
"""
变量名 = []
变量名 = list()
"""

lista = [1, 2, 3]
print(lista[1])

# 查找元素索引
print(lista.index(1))

# 插入
lista.insert(1, 66)
print(lista)

# 追加
lista.append(88)
print(lista)

listb = [99, 100]
lista.extend(listb)
print(lista)

# 删除
del lista[1]
print(lista)

lista.pop(3)
lista.pop(3)
lista.pop(3)
print(lista)

# 清空
lista.clear()
print(lista)

# 统计
listc = [1, 2, 3, 2, 4, 2]
count = listc.count(2)
print(f"listc列表的元素中2一共有{count}个")

# 遍历
i = 0
while i < len(listc):
    print(listc[i])
    i += 1

for x in listc:
    print(x)

# 序列切片
my_str = "01234567"
result1 = my_str[:]
print(f"从头取到尾，result:{result1}")

result2 = my_str[::1]
print(f"从头取到尾，步长为1，result:{result2}")

result3 = my_str[1:3:1]
print(f"从1取到3，步长为1，result:{result3}")
