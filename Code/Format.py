""" print("{}: 计算机{}的CPU占用率为{}%".format("2016-12-31","Python",10))
s1 = "{}{}{}".format("圆周率是",3.1415926,"...")
s2 = "圆周率{{{1}{2}}}是{0}".format("无理数",3.1415926,"...") # 调用format()时解析大括号
print(s1)
print(s2) """

s = "Python"
print("{0:30}".format(s)) # 默认左对齐
print("{0:>30}".format(s)) # 右对齐
print("{0:*^30}".format(s)) # 居中且用*填充
print("{0:-^30}".format(s)) # 居中且用-填充
print("{0:3}".format(s))

print("{0:-^20,}".format(1234567890))
print("{0:-^20}".format(1234567890)) # 对比输出
print("{0:-^20,}".format(12345.67890))

print("{0:.2f}".format(12345.67890))
print("{0:H^20.3f}".format(12345.67890))
print("{0:.4}".format(s))

""" 
1. b表示输出整数的二进制方式
2. c表示输出整数对应的Unicode字符
3. d表示输出整数的十进制方式
4. o表示输出整数的八进制方式
5. x表示输出整数的小写十六进制方式
6. X表示输出整数的大写十六进制方式
"""
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425)) 

"""  
1. e表示输出浮点数对应的小写字母e的指数形式
2. E表示输出浮点数对应的大写字母E的指数形式
3. f表示输出浮点数的标准浮点形式
4. %表示输出浮点数的百分形式
"""
print("{0:e},{0:E},{0:f},{0:%}".format(3.14))