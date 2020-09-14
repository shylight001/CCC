n,k = map(int, input().split())
a = list(map(int,input().split()))
t = list(map(int,input().split()))

total = sum([a[i] for i in range(n) if t[i]])
maxSleep = slider = sum([a[i] for i in range(k) if not t[i]])

for i in range(k,n):
  if not t[i]:
    slider += a[i]
  if not t[i-k]:
    slider -= a[i-k]
  maxSleep = max(slider,maxSleep)
print(maxSleep+total)

# for i in range(n-k):
#     if not t[i+k]:
#         slider += a[i+k]
#     if not t[i]:
#         slider -= a[i]
#     maxSleep = max(slider,maxSleep)
#     #print("second loop:",i+k, i)
# print(maxSleep+total)