def process():
    n = input()
    cnt = 0
    for i in range(0, len(n)):
        if n[i] == '4' or n[i] == '7':
            cnt += 1
    if cnt == int(len(n)):
        print("YES")
    else:
        print("NO")
    
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()