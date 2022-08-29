def process():
    s = input()
    s1 = []
    tmp = ""
    for i in range(len(s)):
        if s[i].isalpha():
            s1.append(s[i])
    for i in range(len(s)):
        if s[i].isdigit():
            tmp += s[i]
    #print(a)
    sum = 0
    for c in tmp:
        sum += int(c)
    s1.sort()
    ans = ""
    for c in s1:
        ans += c
    print(ans + str(sum))
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()