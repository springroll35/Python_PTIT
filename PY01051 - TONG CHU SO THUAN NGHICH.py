def digitSum(s):
    sum = 0
    for c in s:
        sum += int(c)
    return sum

def check(n):
    s = str(digitSum(n))
    if len(s) <= 1:
        return 'NO'
    if s != s[::-1]:
        return 'NO'
    return 'YES'

def process():
    n = input()
    print(check(n))
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()