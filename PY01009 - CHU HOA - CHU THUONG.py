def process():
    s = input()
    if int(len(s) / 2) < sum(1 for c in s if c.isupper()):
        print(s.upper())
    else:
        print(s.lower())
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()

