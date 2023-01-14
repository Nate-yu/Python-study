D_country = {"China":"Beijing","USA":"Washington","France":"Paris"}
print(D_country)
""" print(D_country["China"])
D_country["China"] = "BigBeijing"
print(D_country)

Dp = {}
Dp["2^10"] = 1024
print(Dp["2^10"]) """

print(D_country.keys())
print(list(D_country.values()))
print(D_country.items())
print("China" in D_country)
print(D_country.get("USA", "Sydney")) # 美国在字典中存在，则不返回悉尼
print(D_country.get("Australia", "Sydney")) # 澳大利亚在字典中不存在，故返回悉尼

for key in D_country:
    print(key)
    print(D_country.get(key))
