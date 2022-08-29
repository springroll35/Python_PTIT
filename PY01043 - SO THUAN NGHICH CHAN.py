def kt(n):
    if n != n[::-1] or int(len(n)) % 2 == 1:
        return False
    for c in n:
        if int(c) % 2 == 1:
            return False
    return True

def process():
    n = int(input())
    for i in range(22, n, 2):
        if kt(str(i)):
            print(i, end = ' ')
    print()
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()