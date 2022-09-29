def process():
    n = int(input())
    a = []
    ans = []
    cnt = 0
    for i in range(n):
        s = input().split()
        if len(a) == 0 and len(s) == 6:
            ans.append(1)
        a.append(s)
        if len(a) > 1 and len(s) == 6 and len(a[-2]) == 7:
            ans.append(1)
        if len(s) == 7:
            cnt += 1
        if cnt == 4:
            ans.append(2)
            cnt = 0
    print(len(ans))
    for i in ans:
        print(i)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()