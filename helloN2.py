s = input("主字符串：").strip()  # 读取主字符串
t = input("子字符串：").strip()  # 读取子字符串

kongbailiebiao = []#创建空白列表
len_t = len(t)

for i in range(len(s) - len_t + 1):
    if s[i:i+len_t] == t:
        kongbailiebiao.append(str(i))

print(' '.join(kongbailiebiao))