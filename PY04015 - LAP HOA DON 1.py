class HoaDon:
    tien = 0
    def __init__(self, ma, name, cu, moi):
        self.ma = ma
        self.name = name
        tmp = moi - cu
        if tmp <= 50:
            tmp *= 100
            tmp += tmp * 0.02
        elif tmp <= 100:
            tmp = 50 * 100 + (tmp - 50) * 150
            tmp += tmp * 0.03
        else:
            tmp = 50 * 100 + 50 * 150 + (tmp - 100) * 200
            tmp += tmp * 0.05
        self.tien = round(tmp)

    def printf(self):
        print(self.ma, self.name, self.tien)

def process():
    n = int(input())
    a = []
    for i in range(n):
        ma = 'KH{:02d}'.format(i + 1)
        name = input()
        cu = int(input())
        moi = int(input())
        a.append(HoaDon(ma, name, cu, moi))
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