def process():
    d = [0] * 30001
    n = int(input())
    for i in input().split():
        d[int(i)] = 1
    for i in range(1, 30001):
        if d[i] == 0:
            print(i)
            break

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()