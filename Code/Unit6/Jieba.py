import jieba
# str = input("请输入需要分词的文本：")
str = "鸡你太美，噢baby"
print(jieba.lcut(str,cut_all = True))
print(jieba.lcut_for_search(str))