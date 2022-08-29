def check(s):
    for i in range(2, len(s)):
        if s[i] != s[i-2]:
            return 'NO'
    return 'YES'

def process():
    s = input()
    print(check(s))
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()