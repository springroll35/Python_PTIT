def tower(n, a, b, c):
    if n == 1:
        print(str(a) + ' -> ' + str(c))
        return
    tower(n-1, a, c, b)
    tower(1, a, b, c)
    tower(n-1, b, a, c)

def process():
    n = int(input())
    tower(n, 'A', 'B', 'C')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()