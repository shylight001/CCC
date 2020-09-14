n = int(input())
string = input()
prev = string[0]
StoF,FtoS = 0,0 

for i in range(1,len(string)):
    if string[i] != prev:
        if prev == "S":
            StoF += 1
        else:
            FtoS += 1
    prev = string[i]
    
if StoF > FtoS:
    print("YES")  # more flies from Seattle to San Fran
else:
    print("NO")   # less or equal flies from Seattle to San Fran






# input();s=input();print(["NO","YES"][s[0]=="S" and s[-1]=="F"])

    
# # constant time to check
# input();s=input();print(["NO","YES"][s[0]=="S" and s[-1]=="F"])

# # another one liner:
# input(); s = input(); print('NYOE S'[s[-1] != s[0] == 'S'::2])

# # tricks to get the first and the last.
# n = int(input())
# print('YES' if input()[::n - 1] == 'SF' else 'NO')