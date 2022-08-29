def check(s):
    if len(s) % 2 == 0 or s[0] == s[1]:
        return 'NO'
    for i in range(0, len(s), 2):
        if s[i] != s[0]: return 'NO'
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