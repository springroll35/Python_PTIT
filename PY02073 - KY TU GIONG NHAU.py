def process():
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [0] * 1001
    dp[1] = x
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + x, dp[i // 2] + z)
        else:
            dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + y + z)
    print(dp[n])
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()