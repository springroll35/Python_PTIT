def process():
    n = input()
    if int(n) % 7 == 0:
        print(n)
        return
    for i in range(1000):
        sum = int(n) + int(n[::-1])
        if sum % 7 == 0:
            print(sum)
            return
        n = str(sum)
    print(-1)
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()