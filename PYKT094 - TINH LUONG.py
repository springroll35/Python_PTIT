class Salary():
    def __init__(self, maNV, ten, phong, luongCB, ngayCong):
        self.maNV = maNV
        self.ten = ten
        self.phongBan = phong
        self.luong = 0
        if maNV[0] == 'A':
            if int(maNV[1:3]) >= 1 and int(maNV[1:3]) <= 3:
                self.luong = 10 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 4 and int(maNV[1:3]) <= 8:
                self.luong = 12 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 9 and int(maNV[1:3]) <= 15:
                self.luong = 14 * luongCB * ngayCong
            else:
                self.luong = 20 * luongCB * ngayCong
        elif maNV[0] == 'B':
            if int(maNV[1:3]) >= 1 and int(maNV[1:3]) <= 3:
                self.luong = 10 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 4 and int(maNV[1:3]) <= 8:
                self.luong = 11 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 9 and int(maNV[1:3]) <= 15:
                self.luong = 13 * luongCB * ngayCong
            else:
                self.luong = 16 * luongCB * ngayCong
        elif maNV[0] == 'C':
            if int(maNV[1:3]) >= 1 and int(maNV[1:3]) <= 3:
                self.luong = 9 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 4 and int(maNV[1:3]) <= 8:
                self.luong = 10 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 9 and int(maNV[1:3]) <= 15:
                self.luong = 12 * luongCB * ngayCong
            else:
                self.luong = 14 * luongCB * ngayCong
        else:
            if int(maNV[1:3]) >= 1 and int(maNV[1:3]) <= 3:
                self.luong = 8 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 4 and int(maNV[1:3]) <= 8:
                self.luong = 9 * luongCB * ngayCong
            elif int(maNV[1:3]) >= 9 and int(maNV[1:3]) <= 15:
                self.luong = 11 * luongCB * ngayCong
            else:
                self.luong = 13 * luongCB * ngayCong
        self.luong *= 1000

    def printf(self):
        print('{} {} {} {}'.format(self.maNV, self.ten, self.phongBan, self.luong))

def process():
    m = int(input())
    phongBan = {}
    for i in range(m):
        s = input().split(' ', 1)
        phongBan[s[0]] = s[1]
    n = int(input())
    a = []
    for i in range(n):
        maNV = input()
        a.append(Salary(maNV, input(), phongBan[maNV[-2:]], int(input()), int(input())))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()