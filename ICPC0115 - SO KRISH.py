def frac(n):
    tmp = 1
    for i in range(2, n+1):
        tmp = int(tmp * i)
    return tmp

def check(n):
    m = n
    sum = 0
    while(m > 0):
        sum += frac(m % 10)
        m = int(m / 10)
    return sum == n

def process():
    n = int(input())
    if(check(n)):
        print("Yes")
    else:
        print("No")

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()