def process():
    s = input().lower()
    if s[-3:] == ".py":
        print('yes')
    else:
        print('no')
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()
