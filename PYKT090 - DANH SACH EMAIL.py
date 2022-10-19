f = open("CONTACT.in", "r")
a = set()
for i in f.read().splitlines():
    a.add(i.lower())
for i in sorted(a):
    if(i != ''):
        print(i)