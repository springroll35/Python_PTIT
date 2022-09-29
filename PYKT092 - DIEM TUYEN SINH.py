ut = {'1' : 1.5, '2' : 1.0, '3' : 0.0}

class Contestant():
    kq = ' '
    def __init__(self, maTS, ten, diem, danToc, khuVuc):
        self.maTS = maTS
        self.ten = ten
        self.diem = diem
        self.danToc = danToc
        self.khuVuc = khuVuc
        if danToc == 'Kinh':
            self.diem += ut[self.khuVuc]
        else:
            self.diem += ut[self.khuVuc] + 1.5
        if self.diem >= 20.5:
            self.kq = 'Do'
        else:
            self.kq = 'Truot'
    
    def printf(self):
        print('{} {} {:.1f} {}'.format(self.maTS, self.ten, self.diem, self.kq))

def process():
    n = int(input())
    a = []
    for i in range(n):
        maTS = 'TS{:02d}'.format(i + 1)
        a.append(Contestant(maTS, ' '.join([x.title() for x in input().split()]), float(input()), input(), input()))
    a.sort(key = lambda x: x.maTS)
    a.sort(key = lambda x: -x.diem)
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()