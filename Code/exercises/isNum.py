# 参数为一个字符串，如果这个字符串属于整数、浮点数或复数表示，则返回True，否则返回False
def isNum(str):
    if type(str) == int or type(str) == float or type(str) == complex:
        return True
    else:
        return False

def main():
    str = eval(input("请输入字符串："))
    if isNum(str):
        print("{}是数字".format(str))
    else:
        print("{}不是数字".format(str))

main()