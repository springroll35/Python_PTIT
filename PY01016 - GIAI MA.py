def process():
    s = input()
    ans = ""
    for i in range(0, len(s) - 1, 2):
        ans += s[i] * int(s[i+1])
    print(ans)

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()