n = int(input())
a = []
for i in input().split():
	if len(a) == 0:
		a.append(int(i))
	else:
		if (a[-1] + int(i)) % 2 == 0:
			a = a[:-1]
		else:
			a.append(int(i))
print(len(a))