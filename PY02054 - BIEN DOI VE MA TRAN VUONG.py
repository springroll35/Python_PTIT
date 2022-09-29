def process():
    m, n = map(int, input().split())
    a = []
    for i in range(m):
        b = [int(j) for j in input().split()]
        a.append(b)
    if m > n:
        cnt = 0
        for i in range(m):
            if i % 2 == 0:
                cnt += 1
                if cnt > m - n:
                    for j in range(n):
                        print(a[i][j], end = ' ')
                    print()
            else:
                for j in range(n):
                        print(a[i][j], end = ' ')
                print()
    elif n > m:
        for i in range(m):
            for j in range(n):
                if j % 2 == 1:
                    if j - 1 > 2 * (n - m - 1):
                        print(a[i][j], end = ' ')
                else:
                    print(a[i][j], end = ' ')
            print()
    else:
        for i in range(m):
            for j in range(n):
                print(a[i][j], end = ' ')
            print()

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
