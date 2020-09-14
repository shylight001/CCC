
n = int(input())
alist = list(map(int,input().split()))
binary = input() + '0'

previous = '0'
maxx = 0
minx = 200001
pointer = 0
flag = True
for i in range(n):
    if binary[i] == '0' and previous == '0':
        if alist[i] != i+1:
            flag = False
            break
    elif binary[i] == '1' and previous == '0':
        maxx = alist[i]#max(alist[i], maxx)
        minx = alist[i]#max(alist[i], minx)
        pointer = i 
    elif binary[i] == '1' and previous == '1':
        maxx = max(alist[i], maxx)
        minx = min(alist[i], minx)
    elif binary[i] == '0' and previous == '1':
        maxx = max(alist[i], maxx)
        minx = min(alist[i], minx)
        if maxx != i+1 or minx != pointer+1:
            flag = False
            break
    
    previous = binary[i]
print(["NO","YES"][flag]) 


