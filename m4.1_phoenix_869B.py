a, b = map(int, input().split())
if b-a >= 5:
    print(0) 
else:
    res = 1
    for i in range(a+1,b+1):
        res = res * i % 10
    print(res)