def process():
    [n, k] = input().split()
    n, k = int(n), int(k)
    s = "ABCDEFGHIJKLMNOPQSRTUVWXYZ"
    for i in range(n, 0, -1):
        if k == int(2**(i-1)):
            print(s[i-1])
            break
        elif k > int(2**(i-1)):
            k -= int(2**(i-1))
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()
