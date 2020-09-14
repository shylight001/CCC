n = input()
s = input()

#isUp = True if s[0] == "U" else False

x, y, count = 0, 0, 0
for idx in range(len(s)-1):
    if s[idx] == "U":
        y += 1
    elif s[idx] == "R":
        x += 1  
    if x == y and s[idx] == s[idx+1]:
        count += 1
print(count)