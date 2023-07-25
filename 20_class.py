class Student:
    name = None
    gender = None
    Nationlity = None
    age = None

    def say_hi(self):
        print(f"hi,i am {self.name}")


stu = Student()

stu.name = "kingram"

print(stu.name)
stu.say_hi()


# 构造方法
class Person:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("构造函数执行完毕")


p = Person("kingram", "15", "1111111")
print(p.name)


# str 字符串方法
class Bird:
    name = None
    age = None
    # 私有变量
    __private_hobbit = None

    def __private_func(self):
        print("私有方法")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"bird类对象，name={self.name},age={self.age}"

    def __le__(self, other):
        return self.age >= other.age

    def __lt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


b = Bird("gg bond", 11)

print(str(b))

# lt 对象比较大小方法
b2 = Bird("cc bond", 13)
print(b > b2)

# le 比较大小带等于
b3 = Bird("dd bond", 13)
print(b3 >= b2)

# eq 比较两个对象是否相等
b4 = Bird("oo bond", 13)
print(b4 == b3)