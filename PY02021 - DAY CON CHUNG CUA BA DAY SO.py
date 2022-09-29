def process():
    m, n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    x, y, z = 0, 0, 0
    ans = []
    while x < m and y < n and z < k:
        if a[x] == b[y] and b[y] == c[z]:
            ans.append(a[x])
            x += 1
            y += 1
            z += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        else:
            z += 1
    if len(ans) == 0:
        print('NO')
    else:
        for i in ans:
            print(i, end = ' ')
        print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()