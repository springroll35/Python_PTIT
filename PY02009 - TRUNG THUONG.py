def process():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    d = [0] * 1001
    for i in a:
        d[i] += 1
    b = []
    for i in range(1, 1001):
        b.append([d[i], i])
    b.sort(reverse = True)
    for i in b:
        if i[0] == b[0][0]:
            pos = i[1]
        else:
            break
    print(pos)

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
