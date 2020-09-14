n, m = map(int, input().split())
string = input()
for i in range(m):
    l, r, c1, c2 = input().split()
    l, r = int(l),int(r)
    
    string = string[:l-1]+string[l-1:r].replace(c1, c2)+string[r:]  # string concatenations
          
print(string)       
        