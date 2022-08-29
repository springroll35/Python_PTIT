def kt(n):
    for i in range(0, len(n) - 1):
        if n[i] > n[i+1]:
            return False
    return True

def process():
    n = int(input())
    if kt(str(n)):
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