def digitSum(s):
    sum = 0
    for c in s:
        if c.isdigit():
            sum += int(c)
        else:
            sum += int(ord('-') - ord('0'))
    return sum

def process():
    n = input()
    ans = 0
    while len(n) > 1:
        ans += 1
        n = str(digitSum(n))
    print(ans)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()