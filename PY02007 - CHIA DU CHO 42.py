def process():
    n = 0
    d = [0] * 42
    while True:
        s = input().split()
        for c in s:
            d[int(c) % 42] += 1
        n += len(s)
        if n == 10:
            break
    ans = 0
    for i in d:
        if i > 0:
            ans += 1
    print(ans)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()