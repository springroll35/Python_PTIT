def process():
    n = int(input())
    a = []
    d = {}
    for i in range(n-1):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = 1
        else:
            d[u] += 1
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    cnt1, cnt2 = 0, 0
    for i in d.keys():
        if d[i] == 1:
            cnt1 += 1
        elif d[i] == n-1:
            cnt2 += 1
    print('Yes' if cnt1 == n-1 and cnt2 == 1 else 'No')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()