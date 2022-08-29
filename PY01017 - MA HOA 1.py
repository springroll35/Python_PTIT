def process():
    s = input() + "*"
    cnt, ch = 0, s[0]
    for c in s:
        if c == ch:
            cnt += 1
        else:
            print(str(cnt) + ch, end = '')
            cnt, ch = 1, c
    print()
    

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()