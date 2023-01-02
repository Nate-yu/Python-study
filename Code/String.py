""" print('单引号表示可以使用"双引号"作为字符串的一部分')
print("双引号表示可以使用'单引号'作为字符串的一部分")
print('''三引号中可以使用"双引号"
'单引号'
也可以换行''') """

""" name = input("请输入名字：")
print(name) """

""" name = "Python语言程序设计"
print("name[0]: {}".format(name[0]))
print("name[0]: {}, name[7]: {},name[-1]: {}".format(name[0], name[7], name[-1]))
print("name[2:-4]: {}".format(name[2:-4]))
print("name[:6]: {}".format(name[:6]))
print("name[6:]: {}".format(name[6:]))
print("name[:]: {}".format(name[:])) """

""" print("Python\n语言\t程序\t设计") """

print("Python语言"+"程序设计")
name = "Python语言"+"程序设计"+"基础"
print("GOAL!"*3)
print("Python语言" in name)
print("Y" in "Python语言")

print(len(name),"\n",str(name),"\n",ord('P'),"\n",chr(80))

print(hex(255))
print(oct(-255))
str = "Python 语言 程序 设计"
print(str.split())
print(name.center(40,"="))
print("123".zfill(40))
print("-123".zfill(40))
