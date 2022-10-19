s1, s2 = set(), set()
with open(r'DATA1.in') as f1:
    s1 = set(' '.join(f1.readlines()).replace('\n', ' ').split())
with open(r'DATA2.in') as f2:
    s2 = set(' '.join(f2.readlines()).replace('\n', ' ').split())
a, b = set(), set()
for i in s1:
    a.add(i.lower())
for i in s2:
    b.add(i.lower())
print(*sorted(list(a-b)))
print(*sorted(list(b-a)))
