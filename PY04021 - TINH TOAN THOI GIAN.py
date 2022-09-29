class Player:
    time = 0
    def __init__(self, ma, name, vao, ra):
        self.ma = ma
        self.name = name
        self.time = ra[0] * 60 + ra[1] - vao[0] * 60 - vao[1]

    def printf(self):
        print(self.ma, self.name, int(self.time / 60), 'gio', int(self.time % 60), 'phut')

def process():
    n = int(input())
    a = []
    for i in range(n):
        ma = input()
        name = input()
        vao = [int(x) for x in input().split(':')]
        ra = [int(x) for x in input().split(':')]
        a.append(Player(ma, name, vao, ra))
    a = sorted(a, key = lambda x : (-x.time))
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()