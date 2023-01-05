plaincode = input("请输入明文：")
secretcode = ""
print("加密后的暗码为：",end='')
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        secretchar = chr(ord("a") + (ord(p) - ord("a") + 3) % 26) 
        secretcode += secretchar
        print(secretchar,end = '')
    else:
        secretcode += p
        print(p, end='')

print("")
print("解密后的明文为：",end='')
for q in secretcode:
    if ord("a") <= ord(q) <= ord("z"):
        plaincode = chr(ord("a") + (ord(q) - ord("a") - 3) % 26) 
        print(plaincode,end = '')
    else:
        print(q, end='')