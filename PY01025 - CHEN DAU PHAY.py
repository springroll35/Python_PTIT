def process():
    n = int(input())
    print(format(n, ',d'))
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()