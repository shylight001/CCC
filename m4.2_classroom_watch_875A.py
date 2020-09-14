n = int(input())
count, res = 0, []
limit = min(n, len(str(n))*10)

res = [i for i in range(n-limit, n) if n - i == sum(map(int,(str(i))))]

print(len(res))
for i in res:
    print(i)

'''if n >1000000:  # if it is a big number, check from the last few numbers instead from beginning
    limit = 100
else:
    limit = n
'''    
# for i in range(n-limit, n):
#     if n - i == sum(map(int,(str(i)))):
#         res.append(i)