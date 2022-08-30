def digitSum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum
    
def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        b.append([digitSum(i), i])
    b.sort()
    for i in b:
        print(i[1], end = ' ')
    print()

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()
