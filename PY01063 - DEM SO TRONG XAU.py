def process():
    s, num = input(), input()
    print(s.count(num))
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()