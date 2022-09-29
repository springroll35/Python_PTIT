def process():
    m, n = map(int, input().split())
    a = []
    mi, mx = int(10**9), int((-10)**9)
    for i in range(m):
        b = [int(j) for j in input().split()]
        mi = min(mi, min(b))
        mx = max(mx, max(b))
        a.append(b)
    ans = int((-10)**9)
    for i in range(m):
        for j in range(n):
            if a[i][j] == abs(mx - mi):
                ans = max(ans, a[i][j])
    if ans != int((-10)**9):
        print(ans)
        for i in range(m):
            for j in range(n):
                if a[i][j] == ans:
                    print('Vi tri [' + str(i) + '][' + str(j) + ']')
    else:
        print('NOT FOUND')

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
