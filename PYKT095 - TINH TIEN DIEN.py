class TienDien():
    def __init__(self, maKH, ten, loaiHoGD, csd, csc):
        self.maKH = maKH
        self.ten = ' '.join([x.title() for x in ten.split()])
        self.loaiHoGD = loaiHoGD
        self.trongDM = 0
        self.ngoaiDM = 0
        self.vat = 0
        self.tien = 0
        self.gia = {'A' : 100, 'B' : 500, 'C' : 200}
        if csc - csd >= self.gia[self.loaiHoGD]:
            self.trongDM = self.gia[self.loaiHoGD] * 450
            self.ngoaiDM = (csc - csd - self.gia[self.loaiHoGD]) * 1000
            self.vat = self.ngoaiDM // 20
            self.tien = self.trongDM + self.ngoaiDM + self.vat
        else:
            self.trongDM = (csc - csd) * 450
            self.tien = self.trongDM

    def printf(self):
        print('{} {} {} {} {} {}'.format(self.maKH, self.ten, self.trongDM, self.ngoaiDM, self.vat, self.tien))

def process():
    n = int(input())
    a = []
    for i in range(n):
        maKH = 'KH{:02d}'.format(i + 1)
        ten = input()
        s = input().split()
        a.append(TienDien(maKH, ten, s[0], int(s[1]), int(s[2])))
    a.sort(key = lambda x: -x.tien)
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()