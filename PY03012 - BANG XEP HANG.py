from functools import cmp_to_key

class SinhVien:
    def __init__(self, name, acepted, submit):
        self.name = name
        self.acepted = acepted
        self.submit = submit

def cmp(x, y):
    if x.acepted < y.acepted:
        return 1
    elif x.acepted == y.acepted:
        if x.submit > y.submit:
            return 1
        elif x.submit == y.submit:
            if x.name > y.name:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

def process():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        ac, submit = map(int, input().split())
        a.append(SinhVien(s, ac, submit))
    a = sorted(a, key = cmp_to_key(cmp))
    for i in a:
        print(i.name, i.acepted, i.submit)

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()