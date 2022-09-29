def process():
    s = list(str(i) for i in input())
    if len(s) == 1:
        print(-1)
        return
    i = len(s) - 2
    while i >= 0 and s[i] <= s[i+1]:
        i -= 1
    if i < 0:
        print(-1)
        return
    pos = i + 1
    for j in range(i + 1, len(s)):
        if s[j] < s[i] and s[j] > s[pos]:
            pos = j
    s[i], s[pos] = s[pos], s[i]
    if s[0] == '0':
        print(-1)
    else:
        for c in s:
            print(c, end = '')
        print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()