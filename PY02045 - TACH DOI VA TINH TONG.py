def process():
    n = input()
    while len(n) > 1:
        mid = int(len(n) / 2)
        s = int(n[:mid]) + int(n[mid:])
        print(s)
        n = str(s)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()