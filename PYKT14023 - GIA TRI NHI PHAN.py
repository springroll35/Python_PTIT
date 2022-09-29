def process():
    n, q = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(q):
        x, y = map(int, input().split())
        a[x-1] += 1
        a[y] -= 1
    for i in range(1, n):
        a[i] += a[i-1]
    for i in range(n):
        if (a[i] & 1):
            print(1, end = ' ')
        else:
            print(0, end = ' ')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()