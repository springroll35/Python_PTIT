def process():
    s = input()
    x = input()
    k = int(input())
    k -= 1
    print(s[:k] + x + s[k:])
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()