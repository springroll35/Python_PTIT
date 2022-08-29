from math import gcd

def simple(a, b):
    tmp = 0
    for i in range(len(b)):
        tmp = (tmp * 10 + int(b[i])) % a
    return tmp

def process():
    a = int(input())
    b = input()
    c = simple(a, b)
    if a == 0:
        print(b)
    else:
        print(gcd(a, c))

    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()