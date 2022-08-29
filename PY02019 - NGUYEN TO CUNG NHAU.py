from math import gcd

def process():
    n = int(input())
    a = list(int(i) for i in input().split())
    a.sort()
    for i in range(0, n):
        for j in range(i+1, n):
            x = a[i]
            y = a[j]
            if gcd(x, y) == 1:
                print(x, y)
      
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()