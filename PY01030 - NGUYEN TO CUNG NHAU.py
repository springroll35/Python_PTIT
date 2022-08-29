from math import gcd

def process():
    n, k = map(int, input().split())
    cnt = 0
    for i in range(int(10 ** (k-1)), int(10 ** k)):
        if gcd(n, i) == 1:
            cnt += 1
            print(i, end = ' ')
            if cnt % 10 == 0:
                print()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()