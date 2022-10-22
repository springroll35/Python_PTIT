def process():
    n = int(input())
    if n % 11 == 0:
        print('YES')
    else: 
        print('NO')

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()