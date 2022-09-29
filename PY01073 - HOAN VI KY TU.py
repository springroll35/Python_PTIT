from itertools import permutations

def process():
    s = input()
    perm = permutations(s)
    for i in perm:
        print(*i, sep = '')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()