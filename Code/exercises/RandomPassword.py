# 在26个字母大小写和9个数字组成的列表中随机生成10个8位密码
list1 = []
for i in range(65,91):
    list1.append(chr(i))    # 得到大写字母字符并放入列表
for i in range(97,123):
    list1.append(chr(i))    # 得到小写字母字符并放入列表
for i in range(49,58):
    list1.append(chr(i))    # 得到数字字符（1~9）并放入列表

import random
for i in range(10):
    str1 ="".join(random.choices(list1,k=8)) # "".join()函数，将列表中的元素以指定的字符("")连接生成一个新的字符串。
    print('第{}个密码是{}'.format(i+1,str1))