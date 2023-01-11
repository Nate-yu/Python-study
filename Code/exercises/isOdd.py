def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def main():
    num = eval(input("请输入一个整数："))
    if isOdd(num):
        print("{}是奇数".format(num))
    else:
        print("{}是偶数".format(num))   

main()