def process():
    s = input()
    a = []
    d = [0] * 100
    for i in range(0, len(s), 2):
        tmp = int(s[i:i+2])
        if tmp >= 10:
            a.append(tmp)
        d[tmp] += 1
    ans = []
    for i in a:
        if d[i] > 0:
            ans.append(i)
            d[i] = 0
    for i in ans:
        print(i, end = ' ')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()