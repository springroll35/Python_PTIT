import re

class CaThi:
    def __init__(self, id, date, time, room):
        self.id = id
        self.date = date
        self.time = time
        self.room = room
        self.date2 = list(re.split("/", date))
        self.date2.reverse()
        self.date2 = ''.join(self.date)
        tmp = list(re.split(":", time))
        self.time2 = int(tmp[0]) * 60 + int(tmp[1])
    def __str__(self):
        return self.id + " " + self.date + " " + self.time + " " + self.room

a = list()
f = open("CATHI.in", "r")
t = int(f.readline())
for i in range(t):
    id = 'C{:03d}'.format(i + 1)
    date = f.readline().strip()
    time = f.readline().strip()
    room = f.readline().strip()
    a.append(CaThi(id, date, time, room))
a = sorted(a, key=lambda x: (x.date2, x.time2, x.id))
for i in a:
    print(i)