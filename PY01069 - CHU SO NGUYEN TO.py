n = int(input())
x = [0] * n
ans4, ans5, ans6, ans7, ans8, ans9 = [] , [] , [] , [] , [] , []

def printt4():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 4):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[3] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans4.append(tmp)

def gen4(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 3:
            printt4()
        else:
            gen4(i+1)
            
def printt5():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 5):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[4] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans5.append(tmp)

def gen5(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 4:
            printt5()
        else:
            gen5(i+1)
            
def printt6():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 6):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[5] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans6.append(tmp)

def gen6(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 5:
            printt6()
        else:
            gen6(i+1)
            
def printt7():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 7):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[6] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans7.append(tmp)

def gen7(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 6:
            printt7()
        else:
            gen7(i+1)
            
def printt8():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 8):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[7] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans8.append(tmp)

def gen8(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 7:
            printt8()
        else:
            gen8(i+1)
            
def printt9():
    tmp = ""
    cnt = [0] * 4
    for i in range(0, 9):
        if x[i] == 0:
            tmp += str(2)
            cnt[0] += 1
        elif x[i] == 1:
            tmp += str(3)
            cnt[1] += 1
        elif x[i] == 2:
            tmp += str(5)
            cnt[2] += 1
        elif x[i] == 3:
            tmp += str(7)
            cnt[3] += 1
    if tmp[8] != '2' and cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[3] > 0:
        ans9.append(tmp)

def gen9(i):
    for j in range(0, 4):
        x[i] = int(j)
        if i == 8:
            printt9()
        else:
            gen9(i+1)
            

def process():
    gen4(0)
    ans4.sort()
    for i in range(0, int(len(ans4))):
    	print(ans4[i])
    if n >= 5:
    	gen5(0)
    	ans5.sort()
    	for i in range(0, int(len(ans5))):
    		print(ans5[i])
    if n >= 6: 
    	gen6(0)
    	ans6.sort()
    	for i in range(0, int(len(ans6))):
    		print(ans6[i])
    if n >= 7: 
    	gen7(0)
    	ans7.sort()
    	for i in range(0, int(len(ans7))):
    		print(ans7[i])
    if n >= 8: 
    	gen8(0)
    	ans8.sort()
    	for i in range(0, int(len(ans8))):
    		print(ans8[i])
    if n >= 9: 
    	gen9(0)
    	ans9.sort()
    	for i in range(0, int(len(ans9))):
    		print(ans9[i])
    
def main():
	t = 1
	while t > 0:
		process()
		t -= 1
        
if __name__ == '__main__':
    main()