def process():
    n = input()
    sum, pro, cnt = 0, 1, 0
    for i in range(len(n)):
        if i % 2 == 1:
            sum += int(n[i])
        elif n[i] != '0':
            pro *= int(n[i])
            cnt += 1
    print(str(pro) + ' ' + str(sum))
    
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()