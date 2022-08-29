def process():
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for i in range(n):
            a.append(int(input()))
        mi, mx = min(a), max(a)
        if mi == mx:
            print('BANG NHAU')
        else:
            print(mi, mx)

def main():
    process()
        
if __name__ == '__main__':
    main()