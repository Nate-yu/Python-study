def multi(a, *b):
    for i in b:
        a *= i
    return a
print(multi(1,2,3,4,5))
