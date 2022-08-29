def process():
    n = input()
    ans = 1
    for c in n:
        if c != '0':
            ans *= int(c)
    print(ans)
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()