t = int(input())
while t > 0:
    n = int(input())
    s = input() + " "
    ans = len(s)
    mx1 = mx2 = mx3 = -10**18
    a = []
    l = r = 0
    while ans >= 10**4:
        r = l + 10**4
        while s[r] != ' ':
            r -= 1
        x = s[l:r]
        a.append(x)
        l = r
        ans -= len(x)
    if ans > 0:
        a.append(s[l:])
    for i in a:
        tmp = [int(x) for x in i.split()]
        if max(tmp) > mx1:
            mx2, mx3 = mx1, mx2
            mx1 = max(tmp)
            tmp.remove(mx1)
        if max(tmp) > mx2:
            mx3 = mx2
            mx2 = max(tmp)
            tmp.remove(mx2)
        if max(tmp) > mx3:
            mx3 = max(tmp)
            tmp.remove(mx3)
        del tmp
    print(mx1 + mx2 + mx3)
    t -= 1