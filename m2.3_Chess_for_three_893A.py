n = int(input())
playerSum = 3

inspector = 3

loser = None
isPoss = True

for i in range(n):
    winner = int(input())
    if winner == inspector:
        isPoss = False
        break
    loser = playerSum - winner 
    playerSum, inspector = winner + inspector, loser
    
if isPoss:
    print("YES")
else:
    print("NO")
    
  

  
  
  
  
  
  
  
# c=3
# n=int(input())
# for i in range(n):
	# a=int(input())
	# if a==c:
		# print('NO')
		# exit()
	# c=6-c-a
# print('YES')







