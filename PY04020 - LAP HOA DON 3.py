class HoaDon:
    tien = 0
    def __init__(self, ma, ten, sl, donGia, chietKhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tien = donGia * sl - chietKhau

    def printf(self):
        print(self.ma, self.ten, self.sl, self.donGia, self.chietKhau, self.tien)

def process():
    n = int(input())
    a = []
    for i in range(n):
        ma = input()
        ten = input()
        sl = int(input())
        donGia = int(input())
        chietKhau = int(input())
        a.append(HoaDon(ma, ten, sl, donGia, chietKhau))
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