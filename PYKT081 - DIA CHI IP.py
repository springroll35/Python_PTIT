def check(s):
    if len(s) != 4:
        return 'NO'
    for c in s:
        if c.isdigit():
            if int(c) < 0 or int(c) > 255:
                return 'NO'
        else:
            return 'NO'
    return 'YES'

def process():
    s = input().split('.')
    print(check(s))

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()