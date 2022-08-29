def process():
    a, k, n = map(int, input().split())
    l = (int(a / k) + 1) * k
    cnt = 0
    for i in range(l, n+1, k):
        print(i - a, end = ' ')
        cnt += 1
    if cnt == 0:
        print(-1)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()