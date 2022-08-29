if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = sorted(list(map(int, input().split())))
        ans = 0
        for i in range(0, n-2):
            l, r, x = i+1, n-1, a[i]
            while l < r:
                if x + a[l] + a[r] == 0:
                    ans += 1
                    l += 1
                elif x + a[l] + a[r] < 0:
                    l += 1
                else:
                    r -= 1
        print(ans)
        t -= 1


