def process():
    s = input()
    a = []
    for i in range(len(s)):
        a.append(int(s[i]))
    a.reverse()
    for i in range(len(a) - 1):
        if a[i] >= 5:
            a[i+1] += 1
            a[i] = 0
        else:
            a[i] = 0
    a.reverse()
    for i in a:
        print(i, end = "")
    print()

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
    


