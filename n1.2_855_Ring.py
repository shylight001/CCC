n,p,q,r = map(int,input().split())
alist = list(map(int,input().split()))
a,b,c = -1e20,-1e20,-1e20
for i in range(n):
    
    a = max(a, alist[i]*p)
    b = max(b, a+alist[i]*q)
    c = max(c, b+alist[i]*r)
print(c)