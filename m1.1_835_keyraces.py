# list comprehension
s,v1,v2,t1,t2 = [int(i) for i in input().split()]

r1 = s*v1 + 2*t1
r2 = s*v2 + 2*t2

if r1 == r2:
    print("Friendship")
elif r1 < r2:
    print("First")
else:
    print("Second")
