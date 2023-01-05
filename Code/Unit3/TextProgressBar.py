# 文本进度条
import time
""" scale = 10
print("-----执行开始-----")
for i in range(scale + 1):
    a, b = '**' * i, '..' * (scale-i)
    c = (i / scale) * 100
    print("%{:^3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----") """

""" for i in range(101):
    print("\r{:3}%".format(i),end = "") # \r一般用在print()中对要打印的结果做格式化处理， 表示将光标的位置回退到本行的开头位置。
    time.sleep(0.05) """

scale = 50
print("执行开始".center(scale//2,'-'))
t = time.perf_counter() # 以浮点数计算的秒数返回当前的CPU时间
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    t = time.perf_counter() - t
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,t), end = '')
    time.sleep(0.5)
print("\n"+"执行结束".center(scale//2,'-'))