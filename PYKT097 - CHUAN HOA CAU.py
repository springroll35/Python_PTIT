def process():
    try:
        while True:
            s = input().split()
            print(s[0].title(), end = ' ')
            s.pop(0)
            if s[-1] == '.' or s[-1] == '?' or s[-1] == '!':
                s[-2] += s[-1]
                s.pop(len(s) - 1)
            elif not(s[-1].endswith('.') or s[-1].endswith('?') or s[-1].endswith('!')):
                s[-1] += '.'
            print(' '.join([c.lower() for c in s]))
    except:
        print(end = '')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()