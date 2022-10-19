import re

fi = open('DATA.in','r')
s = [i.strip() for i in fi.readlines()]
a = []
for i in s:
    if i != '':
        a.append(i)
b = []
for i in a:
    tmp = re.split("\\s+", i)
    for j in tmp:
        b.append(j)
ans = []
for i in b:
    if not i.isnumeric():
        ans.append(i)
    elif int(i) < -2147483648 or int(i) > 2147483647:
        ans.append(i)
ans = sorted(ans)
for i in ans:
    print(i, end = ' ')
fi.close()