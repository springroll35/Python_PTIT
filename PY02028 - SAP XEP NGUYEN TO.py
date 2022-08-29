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
    for i in range(n-1):
        if isPrime[a[i]] == 0:
            for j in range(i+1, n):
                if a[i] > a[j] and isPrime[a[j]] == 0:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp
    for i in a:
        print(i, end = ' ')
            

    

def main():
    t = 1
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
