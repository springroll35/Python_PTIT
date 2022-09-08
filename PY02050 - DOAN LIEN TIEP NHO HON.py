def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    st = []
    l = []
    for i in range(n):
        while(len(st) > 0 and a[i] >= a[st[-1]]):
            st.pop()
        if len(st) == 0:
            l.append(0)
        else:
            l.append(st[-1] + 1)
        st.append(i)
    
    for i in range(n):
        print(i - l[i] + 1, end = ' ')
    print()
        
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()