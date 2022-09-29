def process():
    n = int(input())
    student = {}
    for i in range(n):
        maSV = input()
        ten = input()
        lop = input()
        student[maSV] = [ten, lop]
    for i in range(n):
        maSV, s = input().split()
        student[maSV].append(2 * s.count('v') + s.count('m'))
    for i in student:
        tmp = 10 - student[i][2]
        if tmp <= 0:
            tmp = '0 KDDK'
        print(i, student[i][0], student[i][1], tmp)

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()