class Contestant():
    def __init__(self, name, date, mon1, mon2, mon3):
        self.name = name
        self.date = date
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        self.point = mon1 + mon2 + mon3
    
    def printf(self):
        print(self.name, self.date, '{:.1f}'.format(self.point))

def process():
    Contestant(input(), input(), float(input()), float(input()), float(input())).printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()