# 读取
def read():
    f = open("filetest/xx", "r", encoding="utf8")
    print(f.read())
    f.close()


# 读取行  返回列表
def readlines():
    f = open("filetest/xx", "r", encoding="utf8")
    print(f.readlines())
    f.close()


# 读取每一行
def readline():
    f = open("filetest/xx", "r", encoding="utf8")
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()


# for 读取每行数据
def readfor():
    f = open("filetest/xx", "r", encoding="utf8")
    for line in f:
        print(f"每行数据：{line}")
    f.close()

read()
readlines()
readline()
readfor()

# with open 可以自动关闭文件对象
with open("filetest/xx", "r", encoding="utf8") as f:
    print(f.readlines())


# 写入文件内容 (覆盖写入)
with open("filetest/testwrite", "w", encoding="utf8") as f:
    f.write("helloworld")
    f.flush()

# 追加写入
with open("filetest/testwrite", "a", encoding="utf8") as f:
    f.write("\nthis is anna")
    f.flush()

"""
kingram
26
待业
['kingram\n', '26\n', '待业']
kingram

26

待业
每行数据：kingram

每行数据：26

每行数据：待业
['kingram\n', '26\n', '待业']
"""