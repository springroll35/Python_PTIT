def process():
    n, k = map(int, input().split())
    mod = int(1e9) + 7
    ans = 0
    tmp = 1
    while k > 0:
        if (k & 1):
            ans = (ans + tmp) % mod
        tmp *= n
        k >>= 1
    print(ans)

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()