""" n = 1 # 全局变量n
def func(a, b):
    n = b # 这个n是在函数内存中新生成的局部变量，不是全局变量
    return a * b
s = func("knock~", 2)
print(s, n) # 测试n值是否改变 """

n = 1 
def func(a, b):
    global n
    n = b 
    return a * b
s = func("knock~", 2)
print(s, n) 