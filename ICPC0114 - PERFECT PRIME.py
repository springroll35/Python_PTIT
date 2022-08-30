from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    s = str(n)
    m = int(s[::-1])
    if (isPrime(n) == False or isPrime(m) == False):
        return False
    sum = 0
    for c in s:
        sum += int(c)
    if isPrime(sum) == False:
        return False
    tmp = '2357'
    for c in s:
        if c not in tmp:
            return False
    return True
    
def process():
    n = int(input())
    if check(n):
        print('Yes')
    else:
        print('No')

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
