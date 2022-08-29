def process():
    n = int(input())
    a = [float(i) for i in input().split()]
    a.sort()
    Sum = 0
    cnt = 0
    for i in range(1, n):
        if a[i] != a[0] and a[i] != a[n - 1]:
            cnt += 1
            Sum += a[i]
    print("{:.2f}".format(float(Sum / cnt)))

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()