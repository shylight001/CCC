n = int(input())
i = 2
count = 1
while i**2 < n:
    if n % i == 0:
        count += 2
    i += 1
if i**2 == n: count += 1 
print(count)
