def process():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]   
    mx = max(a)
    for i in range(n):
        if a[i] == mx:
            a.insert(i, k)
            break
    for i in a:
        if i < 0:
            print(i, end = ' ')
    for i in a:
        if i >= 0:
            print(i, end = ' ')
    print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()