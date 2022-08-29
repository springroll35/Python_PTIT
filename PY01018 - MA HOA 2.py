def process():
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        x = input()
        if x == "0":
            break
        [k, s] = x.split()
        k = int(k)
        ans = ''
        for i in range(len(s)):
            pos = p.find(s[i])
            ans += p[(pos + k) % 28]
            
        print(ans[::-1])
    

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()