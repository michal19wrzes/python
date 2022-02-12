# your code goes here
def silnia(n):
    if n<=1:
        return 1
    elif n > 1:
        return n*silnia(n-1)
D = int(input())
jednosci=[]
dziesiatki=[]
for i in range(D):
    n = int(input())
    
    if len(str(n))>=3:
        jednosci.append(str(0))
        dziesiatki.append(str(0))
        continue
    x = silnia(n)
    jednosci.append(str(x%10))
    if x <=6:
        dziesiatki.append(str(0))
    else:
        dziesiatki.append(str(x%100)[0])
for i in range(D):
    print(dziesiatki[i]+' '+jednosci[i]) 
    