class Player:
    speed = 0
    ma = ''
    def __init__(self, ten, donVi, dich):
        name = [i for i in ten.split()]
        dv = [i for i in donVi.split()]
        tmp = ''
        for i in dv:
            tmp += i[0].upper()
        for i in name:
            tmp += i[0].upper()
        self.ma = tmp
        self.ten = ten
        self.donVi = donVi
        time = dich[0] + dich[1] / 60 - 6
        time = 120 / time
        self.speed = time

    def printf(self):
        print('{} {} {} {} Km/h'.format(self.ma, self.ten, self.donVi, round(self.speed)))

def process():
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        donVi = input()
        dich = [int(x) for x in input().split(':')]
        a.append(Player(ten, donVi, dich))
    a = sorted(a, key = lambda x : (-x.speed))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()