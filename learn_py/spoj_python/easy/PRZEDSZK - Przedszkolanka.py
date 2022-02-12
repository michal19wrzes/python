#PRZEDSZK - Przedszkolanka
#https://pl.spoj.com/problems/PRZEDSZK/

def czynniki(a):
    #return list with dividers
    czyn = []
    for i in range(2,int(a)+1):
        if a%i==0:
            a = a/i
            czyn.append(i)
    return(czyn)
    
    
t = int(input())
for test in range(t):
    b=1#multiple common dividers
    bb =[] #common dividers
    n = input().split()
    c1 = czynniki(int(n[0]))
    c2 = czynniki(int(n[1]))
    
    for i in range(len(c1)):
        for c in range(len(c2)):
            if c1[i]==c2[c]:
                bb.append(c1[i])
                
    for i in range(len(bb)):
        b *= bb[i]

    print(int((int(n[0])*int(n[1]))/int(b)))
