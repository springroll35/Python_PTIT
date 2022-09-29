class LichThi():
    def __init__(self, maCT, maMH, ten, ngay, gio, nhomThi):
        self.maCT = maCT
        self.maMH = maMH
        self.ten = ten
        self.ngay = ngay.split('/')
        self.gio = gio.split(':')
        self.nhomThi = nhomThi
    
    def printf(self):
        print('{} {} {} {} {} {}'.format(self.maCT, self.maMH, self.ten, '/'.join(self.ngay), ':'.join(self.gio), self.nhomThi))

def process():
    m, n = map(int, input().split())
    monHoc = {}
    for i in range(m):
        maMH = input()
        monHoc[maMH] = input()
    a = []
    for i in range(n):
        maCT = 'T{:03d}'.format(i + 1)
        maMH, ngay, gio, nhomThi = input().split()
        a.append(LichThi(maCT, maMH, monHoc[maMH], ngay, gio, nhomThi))
    a.sort(key = lambda x: x.maMH)
    a.sort(key = lambda x: int(x.gio[0] + x.gio[1]))
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