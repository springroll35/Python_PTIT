class Student():
    def __init__(self, maSV, name, mon1, mon2, mon3):
        self.maSV = maSV
        self.name = ' '.join([x.title() for x in name.split()])
        self.point = round((mon1 * 3 + mon2 * 3 + mon3 * 2) / 8.00 + 0.001, 2)

def process():
    n = int(input())
    a = []
    for i in range(n):
        maSV = 'SV{:02d}'.format(i + 1)
        a.append(Student(maSV, input(), float(input()), float(input()), float(input())))
    a.sort(key = lambda x : -x.point)
    rank, cnt = 1, 0
    print('{} {} {:.2f} {}'.format(a[0].maSV, a[0].name, a[0].point, 1))
    for i in range(1, n):
        if a[i].point == a[i-1].point:
            print('{} {} {:.2f} {}'.format(a[i].maSV, a[i].name, a[i].point, rank))
            cnt += 1
        else:
            rank += cnt + 1
            print('{} {} {:.2f} {}'.format(a[i].maSV, a[i].name, a[i].point, rank))
            cnt = 0

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()