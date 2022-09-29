from datetime import date

class HoaDon:
    soNgay = 0
    tien = 0
    def __init__(self, ma, ten, phong, ngayVao, ngayRa, phatSinh):
        self.ma = ma
        self.ten = ten
        self.phong = int(phong)
        date_format = "%d/%m/%Y"
        d0 = date(ngayVao[2], ngayVao[1], ngayVao[0])
        d1 = date(ngayRa[2], ngayRa[1], ngayRa[0])
        delta = abs(d0 - d1)
        self.soNgay = delta.days + 1
        id = phong[0]
        tmp = phatSinh
        if id == '1':
            tmp += 25 * self.soNgay
        elif id == '2':
            tmp += 34 * self.soNgay
        elif id == '3':
            tmp += 50 * self.soNgay
        else:
            tmp += 80 * self.soNgay
        self.tien = tmp

    def printf(self):
        print(self.ma, self.ten, self.phong, self.soNgay, self.tien)

def process():
    n = int(input())
    a = []
    for i in range(n):
        ma = 'KH{:02d}'.format(i + 1)
        ten = input()
        phong = input()
        ngayVao = [int(x) for x in input().split('/')]
        ngayRa = [int(x) for x in input().split('/')]
        phatSinh = int(input())
        a.append(HoaDon(ma, ten, phong, ngayVao, ngayRa, phatSinh))
    a = sorted(a, key = lambda x : (-x.tien))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()