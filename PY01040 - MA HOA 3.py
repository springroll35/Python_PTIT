def process():
    s = input()
    mid = int(len(s) / 2)
    a, b = "", ""
    da, db = 0, 0
    for i in range(mid):
        a += s[i]
        b += s[i + mid]
        da += int(ord(a[i]) - ord('A'))
        db += int(ord(b[i]) - ord('A'))
    a1, b1 = "", ""
    for i in range(mid):
        tmp = int(ord(a[i]) - ord('A')) + da
        tmp %= 26
        a1 += chr(tmp + ord('A'))
        tmp = int(ord(b[i]) - ord('A')) + db
        tmp %= 26
        b1 += chr(tmp + ord('A'))
    ans = ""
    for i in range(mid):
        tmp = int(ord(a1[i]) - ord('A')) + int(ord(b1[i]) - ord('A'))
        tmp %= 26
        ans += chr(tmp + ord('A'))
    print(ans)

    

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()