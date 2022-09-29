def process():
    n = int(input())
    i = 1
    ans = 0
    while i * (i + 1) < 2 * n:
        x = (1.0 * n - i * (i + 1) / 2) / (i + 1)
        if x - int(x) == 0.0:
            ans += 1
        i += 1
    print(ans)

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()