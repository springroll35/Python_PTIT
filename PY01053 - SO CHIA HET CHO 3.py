def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 3 != 0:
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