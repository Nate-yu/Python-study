""" ls = [425, "BIT", [10, "CS"], 424]
print(ls)
print(ls[2][-1][0])
print(list((425, "BIT", (10, "CS"), 424, 425)))
print(list("你好世界！"))
print(list())

lt = ls # lt是ls所对应数据的引用，lt并不包含真实数据
ls[0] = 0
print(lt) """

vlist = list(range(5))
print(vlist)
print(len(vlist[2:]))
print(2 in vlist)
vlist[3] = "python"
print(vlist)
vlist[1:3] = ["bit", "computer"]
print(vlist)
vlist[1:3] = ["new_bit","new_computer",123]
print(vlist)
vlist[1:3] = ["fewer"]
print(vlist)

for e in vlist:
    print(e, end=" ")