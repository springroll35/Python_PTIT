def check(s):
    if ('888' in s) or (s[0] == '8'):
        return 'NO'
    for c in s:
        if c != '6' and c != '8':
            return 'NO'
    return 'YES'

def process():
    s = input()
    print(check(s))
      
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()