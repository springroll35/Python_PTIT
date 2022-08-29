from math import gcd

def process():
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            for k in range(j + 1, b + 1):
                if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(k, i) == 1:
                    print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")


def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()