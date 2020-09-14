n, k = [int(i) for i in input().split()]
arr = [int(j) for j in input().split()]

index = 0  # for arr
A = 0  #arya's candy total
while index < n and k > 0:
    A += arr[index]
    k -= min(A,8)
    A -= min(A,8)

    index += 1
if k > 0:
    print(-1)
else:
    print(index)