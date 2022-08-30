from math import sqrt

isPrime = [0] * 1000001
p = []

def sangnt():
    isPrime[0] = isPrime[1] = 1
    for i in range(2, int(sqrt(10**6) + 1)):
        if isPrime[i] == 1:
            continue
        for j in range(i * i, 1000001, i):
            isPrime[j] = 1
    for i in range(1000001):
        if isPrime[i] == 0:
            p.append(i)

def lowerBound1(l, r, val):
    tmp = -1
    while l <= r:
        mid = int ((l + r) / 2)
        if p[mid] > val:
            r = mid - 1
        else:
            tmp = mid
            l = mid + 1
    return tmp

def main():
    sangnt()
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = -1
    for i in a:
        vt = lowerBound1(0, len(p), i)
        if vt == -1:
            vt += 1
            ans = max(ans, p[vt] - i)
        else:
            ans = max(ans, min(i - p[vt], p[vt + 1] - i))
    print(ans)

        
if __name__ == '__main__':
    main()
