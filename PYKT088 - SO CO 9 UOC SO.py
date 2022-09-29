from math import sqrt

maxn = int(sqrt(10**9)) + 1
isPrime = [0] * maxn
p = []

def sangnt():
    isPrime[0] = isPrime[1] = 1
    for i in range(2, maxn):
        if isPrime[i] == 1:
            continue
        for j in range(i * i, maxn, i):
            isPrime[j] = 1
    for i in range(2, maxn):
        if isPrime[i] == 0:
            p.append(i)

def process():
    n = int(input())
    ans = 0
    for i in p:
        if i**8 > n:
            break
        ans += 1
    for i in range(len(p)):
        if i * i > n:
            break
        for j in range(i + 1, len(p)):
            if (p[i] * p[j]) * (p[i] * p[j]) <= n:
                ans += 1
            else:
                break
    print(ans)

def main():
    t = 1
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()