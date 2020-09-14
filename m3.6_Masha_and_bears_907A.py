arr = list(map(int, input().split()))
res = []
failed = False
for i in range(len(arr)-1):
    if arr[-1] > 2*arr[i]:
        
        failed = True
        break
    res.append(max([arr[-1],arr[i]))
if failed:
    print(-1)
else:
    for i in res:
        print(i)