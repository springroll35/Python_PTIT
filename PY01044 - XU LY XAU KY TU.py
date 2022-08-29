def process():
    s1 = set(input().lower().split())
    s2 = set(input().lower().split())
    ans1 = s1 | s2
    ans2 = s1 & s2
    ans1 = sorted(ans1)
    ans2 = sorted(ans2)
    for i in ans1:
        print(i, end = ' ')
    print()
    for i in ans2:
        print(i, end = ' ')

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()