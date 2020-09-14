n, one, two = map(int, input().split())
clients = list(map(int, input().split()))

two_with_one = 0
denial = 0
for i in range(n):
	if clients[i] == 1:
		if one != 0: 
			one -= 1
		elif two != 0: 	
			two -= 1
			two_with_one += 1
		elif two_with_one != 0:
			two_with_one -= 1 	
		else:
			denial += 1
	elif clients[i] == 2 :
		if two != 0:
			two -= 1
		else:
			denial += 2
print(denial)
