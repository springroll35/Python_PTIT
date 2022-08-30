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
    m, n = map(int, input().split())
    a = []
    for i in range(m):
        b = [int(j) for j in input().split()]
        a.append(b)
    for i in range(m):
        for j in range(n):
            if isPrime[a[i][j]] == 0:
                a[i][j] = 1
            else:
                a[i][j] = 0
            print(a[i][j], end = ' ')
        print()

def main():
    t = 1
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
