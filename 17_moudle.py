
""""
# 模块就是一个py文件

# 导入模块功能
from time import sleep

sleep(5)

# 导入所有功能
from time import *
sleep(5)

# 导入模块起别名
import time as t 
t.sleep(5)
"""

def test():
    print(1+2)

# name变量的内容不会被导出模块
if __name__ == '__main__':
    test()

