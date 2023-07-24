# 函数使用
"""
def 函数名（传入参数）：
    函数体
    return 返回值
"""


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串data的长度为{count}")


my_len("kingram")


def add(x, y, z):
    """
    add 函数可以接收3个参数
    :param x: 一个数字
    :param y: 一个数字
    :param z: 一个数字
    :return: 返回相加的值
    """
    return x + y + z


print(add(1, 2, 3))

# 函数变量作用域
num = 10


def test_b():
    global num  # 设置函数内部的变量为全局变量
    num = 100
    print(num)


test_b()
print(num)

"""
字符串data的长度为7
6
100
100
"""
