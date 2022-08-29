from math import sqrt

isPrime = [0] * 10001

def sangnt():
    isPrime[0] = isPrime[1] = 1
    for i in range(2, int(sqrt(10000) + 1)):
        if isPrime[i] == 1:
            continue
        for j in range(i * i, 10001, i):
            isPrime[j] = 1

n, x = map(int, input().split())
sangnt()
p = []
for i in range(2, 10001):
    if isPrime[i] == 0:
        p.append(i)
ans = []
ans.append(x)
for i in range(1, n+1):
    ans.append(ans[i-1] + p[i-1])
for i in ans:
    print(i, end = ' ')
