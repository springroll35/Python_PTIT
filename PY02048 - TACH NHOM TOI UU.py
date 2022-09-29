def process():
    n, k = map(int, input().split())
    a = sorted([int(i) for i in input().split()])
    ans = 1
    for i in range(1, n):
        if a[i] - a[i-1] > k:
            ans += 1
    print(ans)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()