#GLUTTON - Obżartuchy
#https://pl.spoj.com/problems/GLUTTON/

import math

secondInDay=86400
t = int(input())
for test in range(t):
    n = input().split()
    obzartuchy=[]
    suma=0
    
    for obzar in range(int(n[0])):
        obzartuchy.append(int(input()))
        
    for i in range(len(obzartuchy)):
        suma += secondInDay/obzartuchy[i]
        suma = math.floor(suma)
        
    x = suma%(int(n[1]))
    if x>0:
        print(math.ceil(suma/int(n[1])))
    else:
        print(math.floor(suma/int(n[1])))