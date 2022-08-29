def process():
    a = list(map(float, input().split()))
    n = 1
    while True:
        if a[2] <= a[0] * (1 + a[1] / 100) ** n:
            print(n)
            break
        n += 1

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()