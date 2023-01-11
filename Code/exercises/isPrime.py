from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def main():
    try:
        num = int(input("请输入一个整数："))
        if isPrime(num):
            print("{}是质数".format(num))
        else:
            print("{}不是质数".format(num))
    except ValueError:
        print("输入格式错误。")

main()