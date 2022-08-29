from math import gcd, sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def digitSum(s):
    sum = 0
    for c in s:
        sum += int(c)
    return sum

def check(n):
    if isPrime(digitSum(n)) == False:
        return 'NO'
    for i in range(len(n)):
        if (i % 2 == 0) and (int(n[i]) % 2 == 1):
            return 'NO'
        elif (i % 2 == 1) and (int(n[i]) % 2 == 0):
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