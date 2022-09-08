def process():
    n = int(input())
    a = []
    for i in range(n):
        b = [int(j) for j in input().split()]
        a.append(b)
    k = int(input())
    top, bot = 0, 0
    for i in range(n):
        for j in range(0, i):
            top += a[i][j]
    for i in range(n):
        for j in range(i+1, n):
            bot += a[i][j]
    if abs(top - bot) <= k:
        print('YES')
    else:
        print('NO')
    print(abs(top - bot))

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
