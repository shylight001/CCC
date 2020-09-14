string = input()

total = 0
for i in range(len(string)):
    if string[i] == "A":
        total += string[:i].count('Q') * string[i:].count('Q') 
print(total)        
        
# k=input();print(sum(k[:i].count("Q")*k[i:].count("Q") for i in range(len(k)) if k[i]=="A"))    0