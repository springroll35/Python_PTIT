import re

t = int(input())
tu = []
while t > 0:
    s = input()
    tu.extend(re.findall(r'\w+', s))
    t -= 1
dic = {}
for i in tu:
    if len(i) == 0:
        continue
    if i.lower() not in dic:
        dic[i.lower()] = -1
    else:
        dic[i.lower()] -= 1
ans = sorted(dic.items(), key = lambda x: (x[1], x[0]))
for i in ans:
    print(i[0] + ' ' + str(- int(i[1])))