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
    a = [int(i) for i in input().split()]
    d = [0] * 1000001
    for i in a:
        d[i] += 1
    for i in a:
        if isPrime[i] == 0 and d[i] > 0:
            print(i, d[i])
            d[i] = 0

def main():
    t = 1
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
