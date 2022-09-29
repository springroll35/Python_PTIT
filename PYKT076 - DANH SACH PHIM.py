class Phim():
    def __init__(self, maPhim, theLoai, ngay, ten, soTap):
        self.maPhim = maPhim
        self.theLoai = theLoai
        self.ngay = ngay
        self.ten = ten
        self.soTap = soTap
    
    def printf(self):
        print('{} {} {} {} {}'.format(self.maPhim, self.theLoai, '/'.join(self.ngay), self.ten, self.soTap))

def process():
    m, n = map(int, input().split())
    tl = {}
    for i in range(m):
        maTL = 'TL{:03d}'.format(i + 1)
        tl[maTL] = input()
    a = []
    for i in range(n):
        maPhim = 'P{:03d}'.format(i + 1)
        maTL = input()
        ngay = input().split('/')
        ten = input()
        soTap = int(input())
        a.append(Phim(maPhim, tl[maTL], ngay, ten, soTap))
    a.sort(key = lambda x: -x.soTap)
    a.sort(key = lambda x: x.ten)
    a.sort(key = lambda x: int(x.ngay[2] + x.ngay[1] + x.ngay[0]))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()