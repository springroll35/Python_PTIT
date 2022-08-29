def process():
    n = int(input())
    a, odd, even = [], [], []
    while n != len(odd) + len(even):
        for i in input().split():
            a.append(int(i))
            if int(i) % 2 == 1:
            	odd.append(int(i))
            else:
            	even.append(int(i))
    even.sort()
    odd.sort(reverse = True)
    od, ev = 0, 0
    for i in a:
        if i % 2 == 0:
            print(even[ev], end = ' ')
            ev += 1
        else:
            print(odd[od], end = ' ')
            od += 1

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()