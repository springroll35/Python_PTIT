a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def change(x, k):
    ans = ''
    while (x > 0):
        r = x % k
        ans = a[r] + ans
        x = int(x / k)
    return ans

def process():
    x, k = map(int, input().split())
    print(change(x, k))
      
def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()