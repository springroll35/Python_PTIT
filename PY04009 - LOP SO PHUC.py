def process():
    a, b, c, d = map(int, input().split())
    x = complex(a, b)
    y = complex(c, d)
    z = (x + y) * x
    t = (x + y) ** 2
    a = int(z.real)
    b = int(z.imag)
    ans = ''
    if b < 0:
        ans = str(a) + ' - ' + str(abs(b)) + 'i'
    else:
        ans = str(a) + ' + ' + str(b) + 'i'
    ans = ans + ', '
    print(ans, end = '')
    a = int(t.real)
    b = int(t.imag)
    if b < 0:
        ans = str(a) + ' - ' + str(abs(b)) + 'i'
    else:
        ans = str(a) + ' + ' + str(b) + 'i'
    print(ans)

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()