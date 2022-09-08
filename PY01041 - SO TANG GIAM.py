def check(n):
    if len(n) < 3:
        return False
    cnt = 0
    for i in range(1, len(n) - 1):
        ok = True
        for j in range(0, i):
            if n[j] >= n[j+1]:
                ok = False
        for j in range(len(n) - 1, i, -1):
            if n[j] >= n[j-1]:
                ok = False
        if ok == True:
            cnt += 1
    if cnt == 0:
        return False
    return True

def process():
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()