# 捕获单个异常
try:
    print(name)
except NameError as e:
    print(f"捕获到单个异常{e}")

# 捕获所有异常
try:
    print(name)
except Exception as e:
    print(f"捕获到异常：{e}")


# 异常else finally

try:
    name = "xxx"
    print(name)
except Exception as e:
    print(f"捕获到异常：{e}")
else:
    print("没有异常")
finally:
    print("程序结束")

"""
捕获到单个异常name 'name' is not defined
捕获到异常：name 'name' is not defined
xxx
没有异常
程序结束
"""