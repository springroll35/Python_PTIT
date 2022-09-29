def process():
    n = int(input())
    cnt = 0
    d = [0] * 201
    mx = 0
    while True:
        s = input().split()
        for c in s:
            d[int(c)] += 1
            mx = max(mx, int(c))
        cnt += len(s)
        if cnt == n:
            break
    cnt = 0
    for i in range(1, mx + 1):
        if d[i] == 0:
            cnt += 1
        else:
            mx = i
    if cnt == 0:
        print('Excellent!')
    for i in range(1, mx + 1):
        if d[i] == 0:
            print(i)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()