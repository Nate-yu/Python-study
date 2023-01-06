from random import*
print(random())
print(uniform(1,10),uniform(1,20))
print(randrange(0,100,4)) # 从0开始到100以4递增的元素中随即返回
print(choice(range(100)))
ls = list(range(10))
print(ls)
shuffle(ls)
print(ls)

seed(125)
print("{}.{}.{}".format(randint(1,10),randint(1,10),randint(1,10)))
print("{}.{}.{}".format(randint(1,10),randint(1,10),randint(1,10)))
seed(125)
print("{}.{}.{}".format(randint(1,10),randint(1,10),randint(1,10)))