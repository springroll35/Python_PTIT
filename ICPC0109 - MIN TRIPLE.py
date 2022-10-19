t = int(input())
while t > 0:
    n = int(input())
    s = input() + " "
    ans = len(s)
    mi1 = mi2 = mi3 = 10**18
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
        if min(tmp) < mi1:
            mi2, mi3 = mi1, mi2
            mi1 = min(tmp)
            tmp.remove(mi1)
        if min(tmp) < mi2:
            mi3 = mi2
            mi2 = min(tmp)
            tmp.remove(mi2)
        if min(tmp) < mi3:
            mi3 = min(tmp)
            tmp.remove(mi3)
        del tmp
    print(mi1 + mi2 + mi3)
    t -= 1