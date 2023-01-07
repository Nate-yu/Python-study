# 在程序中预设一个0~100之间的整数，让用户通过键盘输入所猜的数
import random
count = 1
num = random.randint(0,100)
while True:
    try:
        Num = eval(input("请输入一个0~100之间的数："))
        begin, end = 0, 100
        while num != Num:
            if Num > num:
                print("遗憾，太大了！")
                end = Num
                Num = eval(input("请输入一个{}~{}之间的数：".format(begin, end)))
            if Num < num:
                print("遗憾，太小了！")
                begin = Num
                Num = eval(input("请输入一个{}~{}之间的数：".format(begin, end)))
            count += 1
        print("预测{}次，你猜中了！".format(count))
        break
    except:
        print("输入内容必须为整数！")