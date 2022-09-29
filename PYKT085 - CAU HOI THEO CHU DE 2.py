def process():
    n = int(input())
    dic = {}
    a = []
    x = ''
    for i in range(n):
        s = input()
        if len(a) == 0:
            a.append(s)
            if s not in dic:
                dic[s] = 0
        elif len(a) > 0 and len(x) == 0:
            a.append(s)
            if s not in dic:
                dic[s] = 0
        elif len(s) > 0:
            dic[a[-1]] += 1
        x = s
    for i in dic:
        print(i + ':', dic[i])

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()