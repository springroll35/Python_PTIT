def process():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        tmp = ""
        for i in range(len(s)):
            if s[i].isdigit():
                tmp += s[i]
            elif len(tmp) > 0:
                a.append(tmp)
                tmp = ""
        if len(tmp) > 0:
            a.append(tmp)
    a = [int(x) for x in a]
    a.sort()
    for x in a:
        print(x)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()