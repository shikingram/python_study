class A:
    name = None
    age = None

    def say_hi(self):
        print("hi i am a")

class C:
    cc =None
    def c_say_hi(self):
        print("hi i am c")
class B(A,C):
    gender = None

    def b_say_hi(self):
        print("hi i am b")

    def say_hi(self):
        super().say_hi()
        A.say_hi(self)
        print("hi i am b, overwrite say_hi")


a = A()
b =B()
a.say_hi()
# 调用父类复写前的方法
b.say_hi()
b.b_say_hi()
b.c_say_hi()

"""
hi i am a
hi i am a
hi i am a
hi i am b, overwrite say_hi
hi i am b
hi i am c
"""