def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans, pos = int(1e9), 0
    for i in a:
        tmp = 0
        for j in a:
            if i > j:
                tmp += i - j
            else:
                tmp += j - i
        if ans > tmp:
            ans = tmp
            pos = i
    print(ans, pos)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()