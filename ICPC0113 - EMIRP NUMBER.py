from math import sqrt

isPrime = [0] * 1000001

def sangnt():
    isPrime[0] = isPrime[1] = 1
    for i in range(2, int(sqrt(10**6) + 1)):
        if isPrime[i] == 1:
            continue
        for j in range(i * i, 1000001, i):
            isPrime[j] = 1

def check(n):
    s = str(n)
    m = int(s[::-1])
    if (isPrime[n] == 0 and isPrime[m] == 0 and m != n):
        return True
    return False
    
def process():
    d = [0] * 1000001
    n = int(input())
    for i in range(2, n):
        if check(i):
            x = int(str(i)[::-1])
            if d[i] == 0 and d[x] == 0 and x < n:
                print(i, x, end = ' ')
                d[i] = d[x] = 1
    print()

def main():
    t = int(input())
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
