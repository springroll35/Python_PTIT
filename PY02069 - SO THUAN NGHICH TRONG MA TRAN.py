def process():
    m, n = map(int, input().split())
    a = []
    for i in range(m):
        b = [int(j) for j in input().split()]
        a.append(b)
    ans = 0
    for i in range(m):
        for j in range(n):
            if a[i][j] > 10 and a[i][j] == int(str(a[i][j])[::-1]):
                ans = max(ans, a[i][j])
    if ans != 0:
        print(ans)
    for i in range(m):
        for j in range(n):
            if a[i][j] == ans:
                print('Vi tri [' + str(i) + '][' + str(j) + ']')
    if ans == 0:
        print('NOT FOUND')

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
