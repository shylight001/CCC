n = int(input())
arr = [int(i)  for i in input().split()]
isTriangle = False
for f in range(n):
    idx = f
    s = set()
    s.add(idx)
    for count in range(3):
        nextOne = arr[idx]
        if nextOne in s:
            break
        s.add(nextOne-1)
        idx = nextOne-1
    if nextOne-1 == f and len(s) == 3:
        isTriangle = True
        break
if isTriangle:
    print("YES")
else: 
    print("NO")