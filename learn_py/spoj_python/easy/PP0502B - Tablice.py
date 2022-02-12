#PP0502B - Tablice
#https://pl.spoj.com/problems/PP0502B/
t = int(input())
n=[]
 
for x in range(t):
    m=[]
    n = input().split()
    
    x=int(n[0])+1
    while x!=1:
        x-=1
        m.append(n[x])
        
    print(' '.join(m))