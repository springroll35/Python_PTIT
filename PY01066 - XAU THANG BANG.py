def check(s, x):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(x[i]) - ord(x[i-1])):
            return 'NO'
    return 'YES'

def process():
    s = input()
    print(check(s, x))
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()