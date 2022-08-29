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
    b = []
    d = [0] * 1000001
    for i in a:
        if d[i] == 0:
            b.append(i)
            d[i] = 1
    sum = [0] * 1000001
    sum[0] = b[0]
    for i in range(1, len(b)):
        sum[i] = sum[i-1] + b[i]
    for i in range(len(b)):
        if isPrime[sum[i]] == 0 and isPrime[sum[len(b) - 1] - sum[i]] == 0:
            print(i)
            return
    print('NOT FOUND')

def main():
    t = 1
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()