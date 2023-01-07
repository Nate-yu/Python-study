# 用户从键盘输入一行字符，统计并输出其中英文字符、数字、空格和其他字符的个数
string = input("请输入字符串：")
en, num, space, others = 0, 0, 0, 0
for i in string:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        en += 1
    elif '0' <= i <= '9':
        num += 1
    elif i == ' ':
        space += 1
    else:
        others += 1
print("字符串中英文字符个数为{}个，数字的个数为{}个，空格的个数为{}个，其他字符个数为{}个".format(en, num, space, others))