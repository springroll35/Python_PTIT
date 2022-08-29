from math import sqrt

isPrime = [0] * 1000001

def sangnt():
    isPrime[0] = isPrime[1] = 1
    for i in range(2, int(sqrt(10**6) + 1)):
        if isPrime[i] == 1:
            continue
        for j in range(i * i, 1000001, i):
            isPrime[j] = 1

def process():
    n = int(input())
    ans = 0
    for i in range(2, n - 5):
        if (isPrime[i] == 0 and isPrime[i + 2] == 0 and isPrime[i + 6] == 0) or (isPrime[i] == 0 and isPrime[i + 4] == 0 and isPrime[i + 6] == 0):
            ans += 1
    print(ans)

def main():
    t = int(input())
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
