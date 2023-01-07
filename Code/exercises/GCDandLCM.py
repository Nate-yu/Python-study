n1, n2 = eval(input("请输入两个整数[用逗号分隔]："))
gcd = 0
for i in range(1,n1) and range(1,n2):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
lcm = n1 * n2 / gcd
print("{}和{}的最大公约数为：{}，最小公倍数为：{:.0f}".format(n1,n2,gcd,lcm))