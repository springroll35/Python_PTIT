def process():
    s = input()
    if len(s) == 1:
        print(1)
    else:
        print(len(s) - 1)
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()