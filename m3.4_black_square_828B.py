n, m = map(int,input().split())
minx, maxx, miny, maxy, total = 101, 0, 101, 0, 0
for i in range(n):
    string = input()
    for j in range(m):
        if string[j] == "B":
            total += 1
            minx = min(minx,j)
            maxx = max(maxx,j)
            miny = min(miny,i)
            maxy = max(maxy,i)

ans = max(maxx-minx+1,maxy-miny+1)
if ans > min(m,n):
    print(-1)
elif total == 0:
    print(1)
else:
    print(ans**2-total)