n, m = map(int, input().split())
s,t = input()，input()

min_distinct = n
min_distinct_pos = [i for i in range(1,n+1)]
for i in range(m-n+1):
    distinct = 0
    distinct_pos = []
    for j in range(n):
        if s[j] != t[i+j]:
            distinct += 1
            distinct_pos.append(j+1)
    if distinct < min_distinct:
        min_distinct = distinct
        min_distinct_pos = distinct_pos
        
print(min_distinct)
print(*min_distinct_pos)
