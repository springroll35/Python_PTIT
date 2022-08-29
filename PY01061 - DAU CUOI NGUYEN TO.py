from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process():
    s = input()
    if isPrime(int(s[:3])) and isPrime(int(s[-3:])):
        print('YES')
    else:
        print('NO')
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()