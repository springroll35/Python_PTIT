from math import gcd

def process():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    for i in range(n-1):
        for j in range(i+1, n):
            if gcd(a[i], a[j]) == 1:
                print(a[i], a[j])

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()