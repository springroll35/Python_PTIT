def process():
    n = int(input())
    a = set([int(i) for i in input().split()])
    mi, mx = min(a), max(a)
    print(mx - mi + 1 - len(a))

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
