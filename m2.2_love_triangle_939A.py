# First
n = int(input())
arr = [int(i)  for i in input().split()]
isTriangle = False
for f in range(n):
    idx = f
    s = set()
    s.add(idx+1)
    for count in range(3):
        nextOne = arr[idx]
        if nextOne in s:
            break
        s.add(nextOne)
        idx = nextOne-1
    if nextOne == f+1 and len(s) == 3:
        isTriangle = True
        break
if isTriangle:
    print("YES")
else: 
    print("NO")