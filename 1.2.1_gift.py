"""
ID: kevinou1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

account = {} # {"dave": 0, "laura": 0}
#total number of people
NP = int(fin.readline())
#read in names:
for i in range(NP):
    account[fin.readline().strip()] = 0
    
for i in range(NP):
    giver = fin.readline().strip()
    amount, n = map(int, fin.readline().split())
    if n != 0:
        account[giver] -= (amount - amount%n)  # 200 - 2
    for i in range(n):
        receiver = fin.readline().strip()
        account[receiver] += amount//n
        
for i in account: 
    fout.write(f"{i} {account[i]}\n")
    print(i,account[i])

