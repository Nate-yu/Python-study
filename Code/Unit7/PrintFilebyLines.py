""" fname = input("请输入要打开的文件：")
fo = open(fname,"r",encoding="utf-8")
for line in fo.readlines():
    print(line)
fo.close() """

fname = input("请输入要打开的文件：")
fo = open(fname,"r",encoding="utf-8")
for line in fo:
    print(line)
fo.close()