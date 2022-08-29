def process():
    s = input()
    tmp = ""
    a = []
    for i in range(len(s)):
        if s[i].isdigit():
            tmp += s[i]
        elif len(tmp) > 0:
            a.append(tmp)
            tmp = ""
    a = [int(x) for x in a]
    print(min(a))

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()