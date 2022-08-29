def check(n):
    m = n
    sum = 0
    a = []
    while(m > 0):
        sum += m % 10
        a.append(m % 10)
        m = int(m / 10)
    if sum % 10 != 0:
        return False
    a.reverse()
    for i in range(len(a) - 1):
        if abs(a[i] - a[i+1]) != 2:
            return False
    return True

def process():
    n = int(input())
    if(check(n)):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()