def check(v, cnt):
  for i in v:
    if i == cnt:
      return 0
  return 1

def process():
    n = int(input())
    a = [int(i) for i in input().split()]
    v = []
    ans = 0
    for i in a:
        if(check(v, i)):
            cnt = a.count(i)
        if cnt > n / 2:
            print(i)
            return
        v.append(i)
        ans += cnt
        if n - ans < n / 2:
            print('NO')
            return
    print('NO')

def main():
	t = int(input())
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()