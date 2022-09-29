def process():
    n, m = map(int, input().split())
    a, b, ans = [], [], []
    for i in range (n):
        tmp = [int(i) for i in input().split()]
        a.append(tmp)
    for i in range (n):
        tmp = [0] * n
        ans.append(tmp)
    for i in range(m):
        tmp = [0] * n
        b.append(tmp)
        for j in range (n):
            b[i][j] = a[j][i]
        
    for i in range(n):
        for j in range (n):
            for k in range(m):
                ans[i][j] += a[i][k] * b[k][j]
    
    for i in ans:
        for j in i:
            print(j, end = ' ')
        print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()