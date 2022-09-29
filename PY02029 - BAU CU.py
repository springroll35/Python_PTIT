def process():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else: 
            d[i] += 1
    d = sorted(d.items(), key = lambda x : (x[1], -x[0]), reverse = True)
    if d[0][1] == d[-1][1]:
        print('NONE')
    else:
        i = 1
        while (d[i][1] == d[0][1]): 
            i += 1
        print(d[i][0])

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
