from math import gcd

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutGon(self):
        m = gcd(self.x, self.y)
        print(f"{self.x // m}/{self.y // m}")
    
a = [int(i) for i in input().split()]
p = PhanSo(a[0], a[1])
p.rutGon()