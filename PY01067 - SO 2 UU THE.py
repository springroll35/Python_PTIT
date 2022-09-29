from queue import Queue

def process():
    n = int(input())
    q = Queue()
    q.put('1')
    q.put('2')
    d = 0
    while q.qsize() > 0:
        u = q.get()
        cnt = u.count('2')
        if 2 * cnt > len(u):
            d += 1
            if d > n:
                break
            print(u, end = ' ')
        q.put(u + '0')
        q.put(u + '1')
        q.put(u + '2')
    print()

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()