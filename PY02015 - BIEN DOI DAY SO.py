def change(a, b, c, d):
    cnt = 0
    while not(a == b and b == c and c == d):
        cnt += 1
        aa = abs(a - b)
        bb = abs(b - c)
        cc = abs(c - d)
        dd = abs(d - a)
        a, b, c, d = aa, bb, cc, dd
    return cnt

def process():
    while True:
        a, b, c, d = map(int, input().split())
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        print(change(a, b, c, d))


def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
