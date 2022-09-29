def process():
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    print(max([a[0] * a[1], a[0] * a[1] * a[-1], a[-1] * a[-2], a[-1] * a[-2] * a[-3]]))

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()