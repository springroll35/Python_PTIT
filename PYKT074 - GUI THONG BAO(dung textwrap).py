import textwrap

def process():
    s = input()
    print(textwrap.shorten(s, width = 100, placeholder = ''))

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()