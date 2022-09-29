class GiaoVien:
    diem = 0
    mon = ''
    kq = ''
    def __init__(self, maGV, ten, maXT, tinHoc, chuyenMon):
        self.maGV = maGV
        self.ten = ten
        a, b = maXT[0], maXT[1]
        if a == 'A':
            self.mon = 'TOAN'
        elif a == 'B':
            self.mon = 'LY'
        else:
            self.mon = 'HOA'
        self.diem = tinHoc * 2 + chuyenMon
        if b == '1':
            self.diem += 2.0
        elif b == '2':
            self.diem += 1.5
        elif b == '3':
            self.diem += 1.0
        if self.diem >= 18:
            self.kq = 'TRUNG TUYEN'
        else:
            self.kq = 'LOAI'

    def printf(self):
        print('{} {} {} {:.1f} {}'.format(self.maGV, self.ten, self.mon, self.diem, self.kq))

def process():
    n = int(input())
    a = []
    for i in range(n):
        maGV = 'GV{:02d}'.format(i + 1)
        ten = input()
        maXT = input()
        tinHoc = float(input())
        chuyenMon = float(input())
        a.append(GiaoVien(maGV, ten, maXT, tinHoc, chuyenMon))
    a = sorted(a, key = lambda x : (-x.diem))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()