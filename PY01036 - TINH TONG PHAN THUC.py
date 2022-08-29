def process():
    n = int(input())
    ans = 0
    for i in range(2 - n % 2, n + 1, 2):
        ans += 1/i
    print('{:.6f}'.format(ans))
    

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()