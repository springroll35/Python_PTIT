def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = [0] * 1000001
    for i in range(n):
        d[a[i]] += 1
    for i in a:
        if (d[i] & 1):
            print(i)
            return

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()