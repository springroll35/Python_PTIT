def process():
    n, p = map(int, input().split())
    ans = 0
    for i in range(2, n + 1):
        j = i
        while j % p == 0:
            j //= p
            ans += 1
    print(ans)

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()