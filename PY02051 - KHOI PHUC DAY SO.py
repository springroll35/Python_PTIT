def process():
    n = int (input())
    a = []
    for i in range(n):
        sum = 0
        for j in input().split():
            sum += int(j)
        a.append(sum)
    if n == 1:
        print (a[0])
    elif n == 2:
        print(sum // 2, sum // 2)
    else:
        sum = 0
        for i in a:
            sum += i
        sum = sum // (int(n - 1) * 2)
        for i in a:
            print(int((i - sum) / (n - 2)), end = ' ')

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()