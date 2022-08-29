def process():
    n = int(input())
    for i in range(1, n + 1):
        s1, s2 = input(), input()
        print('Test ' + str(i) + ': ', end = '')
        if (len(s1) != len(s2)):
            print('NO')
            continue
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            print('YES')
        else:
            print('NO')
      
def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()