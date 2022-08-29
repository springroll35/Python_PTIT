from math import sqrt, gcd

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process():
    n = int(input())
    ans = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            ans += 1
    if(isPrime(ans)):
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