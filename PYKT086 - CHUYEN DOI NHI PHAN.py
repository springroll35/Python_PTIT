def ch(n):
    if n < 10:
        return str(n)
    if n == 10:
        return 'A'
    if n == 11:
        return 'B'
    if n == 12:
        return 'C'
    if n == 13:
        return 'D'
    if n == 14:
        return 'E'
    if n == 15:
        return 'F'
    
def change(n, b):
    while len(n) % b != 0:
        n = '0' + n
    ans = ''
    for i in range(len(n) - 1, 0, -b):
        num, tmp = 0, 1
        for j in range(i, i-b, -1):
            if j >= 0:
                num += tmp * int(n[j])
                tmp *= 2
        ans += ch(num)
    return ans[::-1]   
      
fi = open("DATA.in", "r")
t = int(fi.readline())
while t > 0:
    n = int(fi.readline())
    s = fi.readline()
    s = s[:len(s)-1]
    if n == 2:
        print(s)
    elif n == 4:
        print(change(s, 2))
    elif n == 8:
        print(change(s, 3))
    else:
        print(change(s, 4))
    t -= 1
fi.close()