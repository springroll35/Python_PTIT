def process():
    n = int(input())
    dic = {}
    while n > 0:
        s = input()
        dic[s] = 1
        n -= 1
    print(len(dic))


def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()