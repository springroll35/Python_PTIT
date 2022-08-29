v = []
maxn = int(10**18)

def init():
    i, j, k = 1, 1, 1
    while int(i) <= maxn:
        while int(i * j) <= maxn:
            while int(i * j * k) <= maxn:
                v.append(i * j * k)
                k = int(k * 2)
            j = int(j * 3)
            k = 1
        i = int(i * 5)
        j = 1
    v.sort()
    
def process():
    n = int(input())
    l, r = 0, len(v) - 1
    while l <= r:
        mid = int(l + (r - l) / 2)
        if v[mid] >= n:
            r = mid - 1
        else:
            l = mid + 1
    x = v[int(l)]
    if(l == len(v) or x != n):
    	print("Not in sequence")
    else:
    	print(l+1)
    
def main():
	t = int(input())
	init()
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()