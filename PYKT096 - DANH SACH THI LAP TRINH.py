class Contestant():
    def __init__(self, maTS, ten, team, uni):
        self.maTS = maTS
        self.ten = ten
        self.team = team
        self.uni = uni
    
    def printf(self):
        print(self.maTS, self.ten, self.team, self.uni)

def process():
    m = int(input())
    doi = {}
    for i in range(m):
        maTeam = 'Team{:02d}'.format(i + 1)
        doi[maTeam] = [input(), input()]
    n = int(input())
    a = []
    for i in range(n):
        maTS = 'C{:03d}'.format(i + 1)
        ten = input()
        maTeam = input()
        a.append(Contestant(maTS, ten, doi[maTeam][0], doi[maTeam][1]))
    a.sort(key = lambda x: x.ten)
    for i in a:
        i.printf()

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()