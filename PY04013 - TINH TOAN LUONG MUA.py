def time(x, y):
    return y[0] * 60 + y[1] - x[0] * 60 - x[1]

def process():
    dic = {}
    n = int(input())
    for i in range(n) :
        name = input()
        x = [int(i) for i in input().split(':')]
        y = [int(i) for i in input().split(':')]
        mua = int(input())
        if name not in dic:
            dic[name] = (time(x, y), mua)
        else:
            dic[name] = (dic[name][0] + time(x, y), dic[name][1] + mua)
    cnt = 1
    for i in dic:
        print('T{:02d}'.format(cnt), i, "{:.2f}".format(dic[i][1] * 60 / dic[i][0]))
        cnt += 1

def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()