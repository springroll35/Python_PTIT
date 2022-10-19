import re

fi = open('VANBAN.in','r')
s = [i.strip() for i in fi.readlines()]
words = []
ans = {}
for i in s:
    tmp = re.split("\\s+", i)
    for j in tmp:
        tmp1 = j[::-1]
        if tmp1 == j:
            words.append(j)
for i in words:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
mx = -1
for i in ans:
    if len(i) > mx:
        mx = len(i)
for i in ans:
    if len(i) == mx:
        print(i, ans[i])
fi.close()