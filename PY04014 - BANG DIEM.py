from decimal import ROUND_HALF_UP, Decimal

id = 1

class Student():
    maHS = 'HS'
    diemTB = 0.0
    xepLoai = ''
    def __init__(self, name, diem):
        global id
        self.maHS += '{:02d}'.format(id)
        id += 1
        self.name = name
        sum = 0
        for i in range(10):
            if i < 2:
                sum += 2 * diem[i]
            else:
                sum += diem[i]
        sum /= 12
        self.diemTB = sum.quantize(Decimal('0.1'), ROUND_HALF_UP)
        if sum < 5:
            self.xepLoai = 'YEU'
        elif sum < 7:
            self.xepLoai = 'TB'
        elif sum < 8:
            self.xepLoai = 'KHA'
        elif sum < 9:
            self.xepLoai = 'GIOI'
        else:
            self.xepLoai = 'XUAT SAC'

    def printf(self):
        print(self.maHS, self.name,'{:.1f}'.format(self.diemTB), self.xepLoai)

def process():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        tmp = [Decimal(x) for x in input().split()]
        a.append(Student(s, tmp))
    a = sorted(a, key = lambda x : (-x.diemTB, x.maHS))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()