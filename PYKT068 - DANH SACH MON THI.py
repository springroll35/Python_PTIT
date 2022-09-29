from functools import cmp_to_key

class MonHoc:
    def __init__(self, maMon, mon, hinhThuc):
        self.maMon = maMon
        self.mon = mon
        self.hinhThuc = hinhThuc

def cmp(x, y):
    if x.maMon > y.maMon:
        return 1
    return -1

def process():
    n = int(input())
    a = []
    for i in range(n):
        maMon = input()
        mon = input()
        hinhThuc = input()
        a.append(MonHoc(maMon, mon, hinhThuc))
    a = sorted(a, key = cmp_to_key(cmp))
    for i in a:
        print(i.maMon, i.mon, i.hinhThuc)

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()