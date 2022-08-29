from math import gcd, sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def digitSum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

def process():
    [a, b] = input().split()
    a, b = int(a), int(b)
    sum = int(digitSum(gcd(a, b)))
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()