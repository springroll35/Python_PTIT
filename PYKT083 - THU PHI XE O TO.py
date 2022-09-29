def process():
    n = int(input())
    dic = {}
    for i in range(n):
        s = input().split()
        if s[4] not in dic:
            dic[s[4]] = 0
        if s[3] == 'IN':
            if s[1] == 'Xe_con':
                if s[2] == '5':
                    dic[s[4]] += 10000
                else:
                    dic[s[4]] += 15000
            elif s[1] == 'Xe_tai':
                dic[s[4]] += 20000
            else:
                if s[2] == '29':
                    dic[s[4]] += 50000
                else:
                    dic[s[4]] += 70000
    for i in dic:
        print(i + ':', dic[i])


def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()