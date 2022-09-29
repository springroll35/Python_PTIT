from itertools import permutations

def process():
    n = int(input())
    a = [int(i) for i in range(1, n + 1)]
    perm = permutations(a)
    ans = []
    for i in perm:
        ans.append(i)
    ans.sort(reverse = True)
    print(len(ans))
    for i in ans:
        tmp = ''
        for j in i:
            tmp += str(j)
        print(tmp, end = ' ')
    print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()