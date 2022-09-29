def process():
    m, n = map(int, input().split())
    a = set([int(i) for i in input().split()])
    b = set([int(i) for i in input().split()])
    print(*sorted(a & b))
    print(*sorted(a - b))
    print(*sorted(b - a))

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()