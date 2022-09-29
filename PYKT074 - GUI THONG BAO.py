def process():
    s = input()
    if len(s) <= 100:
        print(s)
    else:
        n = 100
        while s[n - 1] != ' ':
            n -= 1
        for i in range(n):
            print(s[i], end = '')
        print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()