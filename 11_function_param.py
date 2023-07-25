# 函数传参方式

# 位置参数
def user_info(name, age, gender):
    print(f"姓名：{name}年龄：{age}性别：{gender}")


user_info("kingram", "25", "男")

# 关键字参数
user_info(name="kingram", age="25", gender="男")


# 默认参数 (默认参数设置默认在最后，后面所有参数都必须给默认值)
def user_info2(name, age, gender="男"):
    print(f"姓名：{name}年龄：{age}性别：{gender}")


user_info2("kingram", "25")


# 不定长参数
# 元组传递
def user_info3(*args):
    print(args)


user_info3("kingram", "12", 18)


# 字典传递
def user_info4(**kwargs):
    print(kwargs["name"])


user_info4(name="kingram", age=18, gender="男")


# 函数作为参数
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)

# 匿名函数传参

test_func(lambda x, y: x + y)
