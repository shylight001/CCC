n=int(input())
a=[int(x) for x in input().split()]
s=input()+'0'
m=0
for i in range (n):
    m=max(m,a[i])
    if s[i]=='0' and m>i+1:
        print("NO")
        quit()
print('YES')