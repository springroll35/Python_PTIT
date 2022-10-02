from math import gcd, sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    if isPrime(int(n[-4:])):
        return 'YES'
    return 'NO'

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