from bisect import bisect_left as lower_bound

def getSum(t, x):
    sum = 0
    while x > 0:
        sum += t[x]
        x -= x & (-x)
    return sum

def update(t, n, x, val):
    while x <= n:
        t[x] += 1
        x += x & (-x)

def convert(a, n):
	tmp = [0] * n
	for i in range(n):
		tmp[i] = a[i]
	tmp = sorted(tmp)
	for i in range(n):
		a[i] = lower_bound(tmp, a[i]) + 1

def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    convert(a, n)
    BIT = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        ans += getSum(BIT, a[i] - 1)
        update(BIT, n, a[i], 1)
    print(ans)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()