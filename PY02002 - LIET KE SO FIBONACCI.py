def process():
    [a, b] = input().split()
    a, b = int(a), int(b)
    f = [0] * (b+1)
    f[0] = 0
    f[1] = f[2] = 1
    for i in range(3, b+1):
        f[i] = int(f[i-1] + f[i-2])
    for i in range(a, b+1):
        print(str(f[i]) + ' ', end = "")
    print()
    

def main():
    t = int(input())
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()