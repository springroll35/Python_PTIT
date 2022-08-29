def main():
    s = input()
    n = len(s)
    k = int(input())
    if(n & 1):
        s = s[:n]
    i, v = 0, []
    while i < n:
        v.append(int(s[i:i+2]))
        i += 2
    a = sorted(set(v))
    cnt = 0
    for i in a:
        if(v.count(i) >= k):
            print(str(i) + ' ' + str(v.count(i)))
        else:
            cnt += 1
    if(cnt == len(a)):
        print("NOT FOUND")


if __name__ == '__main__':
    main()
    


