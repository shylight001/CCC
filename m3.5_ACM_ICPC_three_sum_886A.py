lst = list(map(int, input().split()))

def sol():
  target = sum(lst)/2
  if target.is_integer():
      for i in range(len(lst)-2):
          for j in range(i+1,len(lst)-1):
              for k in range(j+1,len(lst)):
                  if lst[i]+lst[j]+lst[k] == int(target):
                      return "YES"
  return "NO"
print(sol())



from itertools import permutations
print(['NO','YES'][any(sum(x[:3]) == sum(x[3:]) for x in permutations(map(int, input().split())))])