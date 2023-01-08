""" def dup(str, times = 2):
    print(str*times)
dup("knock~")
dup("knock~",4)

def vfunc(a, *b):
    print(type(b))
    for n in b:
        a += n
    return a
print(vfunc(1,2,3,4,5)) """

def func(a, b):
    return b,a
s = func("knock~",2)
print(s, type(s))
