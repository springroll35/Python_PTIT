def process():
    s = input().split(' ')
    for x in s:
        print(x)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()