print("hello")
print('hello')
print("""hello""")

name = "kingram"
age = 11
print("my name is ： %s ,my age is : %s" % (name, age))

# 精度控制
money = 12.222222
print("money is %.2f" % money)

# 快速格式化
dd = "qz"
ddage = 12
ddhigh = 80.3
print(f"ddname={dd},ddage={ddage},ddhigh={ddhigh}")

# 格式化表达式
print(f"10.1 * 10.1 的结果是{10.1 *10.1}")

"""
hello
hello
hello
my name is ： kingram ,my age is : 11
money is 12.22
ddname=qz,ddage=12,ddhigh=80.3
10.1 * 10.1 的结果是102.00999999999999
"""