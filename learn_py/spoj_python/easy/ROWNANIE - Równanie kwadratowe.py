#ROWNANIE - Równanie kwadratowe
#https://pl.spoj.com/problems/ROWNANIE/
def delta(a,b,c):
    d = pow(float(b),2)-(4*float(a)*float(c))
    return d

while True:
    n = input().split()
    if delta(n[0],n[1],n[2]) >0:
        print(2)
        continue
    if delta(n[0],n[1],n[2])==0:
        print(1)
        continue
    else:
        print(0)

