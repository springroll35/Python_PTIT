def process():
    n = int(input())
    a = [''] * n
    b, c = [0] * n, [0] * n
    for i in range(n):
        a[i] = input()
        for j in range(n):
            if a[i][j] == 'C':
                b[i] += 1
                c[j] += 1
    ans = 0
    for i in range(n):
        ans += (b[i] * (b[i] - 1) // 2) + (c[i] * (c[i] - 1) // 2)
    print(ans)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()