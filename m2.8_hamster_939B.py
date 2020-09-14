n, k = map(int, input().split())
types = list(map(int,input().split()))

least = n % types[0]
tp_box = 1
# find min/max algorithm
for i in range(1, k):
	remainder = n % types[i]
	
	if remainder < least:
		least = remainder
		tp_box = i + 1
        
num_box = n // (types[tp_box-1])
print(tp_box, num_box)