import re

def process():
    s = ''
    while True:
        try:
            s += input()
        except EOFError:
            break
    s = re.split('[.?!]', s)
    for i in s:
        if len(i) > 0:
            x = re.sub('\s+', ' ', i.strip())
            print(x[0].upper() + x[1:].lower())

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()