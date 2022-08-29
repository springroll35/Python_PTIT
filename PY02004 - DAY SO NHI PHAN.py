def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()