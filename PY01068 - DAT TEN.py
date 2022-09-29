from itertools import combinations

def process():
    n, k = map(int, input().split())
    a = set([i for i in input().split()])
    a = sorted(a)
    com = combinations(a, k)
    for i in com:
        print(*i, sep = ' ')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()