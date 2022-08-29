def process():
    n, d = map(int, input().split())
    l = input().split()
    pos = d % n
    for i in range(pos, n):
        print(l[i], end = ' ')
    for i in range(d):
        print(l[i], end = ' ')
    print()
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()