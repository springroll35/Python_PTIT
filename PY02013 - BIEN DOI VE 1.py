def process():
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        while n != 1:
            if (n & 1):
                n = n * 3 + 1
            else:
                n //= 2
            a.append(n)
        a = set(a)
        print(len(a) + 1)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()