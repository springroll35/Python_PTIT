rc = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def process():
    m, n = map(int, input().split())
    a = []
    q = []
    for i in range(m):
        a.append(list(int(i) for i in input().split()))
        for j in range(n):
            if a[i][j] == -1:
                q.append([i, j])
    ans = 0
    while len(q) > 0:
        u = q[0]
        q.pop(0)
        for i in rc:
            x = u[0] + i[0]
            y = u[1] + i[1]
            if x >= 0 and y >= 0 and x < m and y < n and a[x][y] != 0:
                ans += a[x][y]
                a[x][y] = 0
    print(ans)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()