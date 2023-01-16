# 接收字符串，按字符出现的频率降序打印字母。
str = input("请输入字符串：")
len1 = len(str) # 获取字符串长度

list1 = []
for i in range(len1): # 将输入的字符串转换成列表
    list1.append(str[i])

counts = {}

for ch in  list1:
    """ if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1 """
    counts[ch] = counts.get(ch,0) + 1 # 如果ch在counts中存在，则返回ch对应的值，否则返回0
items = list(counts.items()) # 将字典转换为记录列表
items.sort(key=lambda x:x[1],reverse=True) # 以记录第二列排序

set1 = set(str)
len2 = len(set1) # 利用set获取字符种类
for i in range(len2):
    ch, count = items[i]
    print("{0:<10}{1:>5}".format(ch,count))
