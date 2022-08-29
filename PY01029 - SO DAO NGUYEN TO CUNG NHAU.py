from math import gcd, sqrt

def process():
    n = input()
    m = n[::-1]
    n = int(n)
    m = int(m)
    if gcd(m, n) == 1:
        print('YES')
    else:
        print('NO')
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()