
def isRepetitive(list1):
    set1 = set(list1)
    len1 = len(list1)
    len2 = len(set1)
    if len1 > len2:
        return True
    else:
        return False

list1 = ["a","aa","aaa","a","aa"]
print("原列表为：{}".format(list1))
if isRepetitive(list1):
    print("列表中存在重复元素")
else:
    print("列表中不存在重复元素")