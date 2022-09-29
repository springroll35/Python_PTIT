from math import gcd

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutGon(self):
        m = gcd(self.x, self.y)
        print(f"{self.x // m}/{self.y // m}")
    
a = [int(i) for i in input().split()]
p1 = PhanSo(a[0], a[1])
p2 = PhanSo(a[2], a[3])
p = PhanSo(p1.x * p2.y + p2.x * p1.y, p1.y * p2.y)
p.rutGon()