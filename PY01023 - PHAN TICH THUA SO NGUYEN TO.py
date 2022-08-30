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
    ans = '1'
    for i in range(2, int(sqrt(n)) + 1):
        cnt = 0
        while n % i == 0:
            n = n / i
            cnt += 1
        if cnt > 0:
            ans = ans + " * " + str(i) + "^" + str(cnt)
    if n > 1:
        ans = ans + " * " + str(int(n)) + "^1" 
    print(ans)

def main():
    t = int(input())
    sangnt()
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
