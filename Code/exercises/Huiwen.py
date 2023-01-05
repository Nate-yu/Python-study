# 判断回文数
num = input("请输入要判断的数(5位)：")
if num[0] == num[4] and num[1] == num[3]:
    print("{}是一个回文数".format(num))
else:
    print("{}不是一个回文数".format(num)) 