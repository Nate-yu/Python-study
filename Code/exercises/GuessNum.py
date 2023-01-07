# 在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜的数
import random
count = 1
num = random.randint(0,9)
Num = eval(input("请输入一个0~9之间的数："))
while num != Num:
    if Num > num:
        print("遗憾，太大了！")
    if Num < num:
        print("遗憾，太小了！")
    Num = eval(input("请输入一个0~9之间的数："))
    count += 1
print("预测{}次，你猜中了！".format(count))