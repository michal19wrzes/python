#https://pl.spoj.com/submit/PA05_BIB/
import numpy as np
t = int(input())
for test in range(t):

    n = int(input()) #liczba plikow
    # nd = np.array(input().split(),float)
    # moves = []
    # for i in range(n-1):
    #     min1 = np.amin(nd)
    #     ind1 = np.where(nd == min1)[0][0]
    #     nd[ind1] = float('inf')
    #     moves.append(ind1)

    #     min2 = np.amin(nd)
    #     ind2 = np.where(nd == min2)[0][0]
    #     nd[ind2] = float('inf')
    #     moves.append(ind2)

    #     nd[ind1] = min1+min2

    # print(int(nd[ind1]))
    # [print(f"{moves[m]+1} {moves[m+1]+1}") if moves[m]+1<=moves[m+1]+1 else print(f"{moves[m+1]+1} {moves[m]+1}") for m in range(0,len(moves),2)]
    nd = np.array(input().split(),int)
    nd = list(nd)
    print(sum(nd))
    moves = []
    for i in range(n-1):
        min1 = min(nd)
        ind1 = nd.index(min1)
        nd[ind1] = float('inf')
        #print(ind1+1)
        min2 = min(nd)
        ind2 = nd.index(min2)
        nd[ind2] = float('inf')
        nd[ind1] = min1 + min2
        if ind1<=ind2:
            print(f"{ind1+1} {ind2+1}")
        else:
            print(f"{ind2+1} {ind1+1}")
#NZEC FAIL:
t = int(input())
for test in range(t):
    n = int(input())
    lista1 = [7,1,4,12,6,3,9,12,13,24,25,13,2,5,6,7,26,47,57,68,79,80,90,95,94]
    lista2 = [x for x in sorted(lista1)]
    wyn = []
    suma=0
    for i in range(n-1):
        if i==0:
            min1,min2 = lista2[i],lista2[i+1]
            ind1 = lista1.index(min1)
            lastInd = ind1
            ind2 = lista1.index(min2)
            lista2[i] = min1+min2
            last = lista2[i]
            suma+= last
            lista2[i+1]=float('inf')
            wyn.append([ind1,ind2])
        elif last<lista2[i+1]:
            min1,min2 = last,lista2[i+1]
            ind1 = lastInd
            ind2 = lista1.index(min2)
            lista2[lastInd] = min1 + min2
            last = lista2[lastInd]
            lista2[i+1] = float('inf')
            suma += last
            wyn.append([ind1,ind2])
        else:
            min1,min2 = lista2[i+1],last
            ind1 = lista1.index(min1)
            ind2 = lastInd
            lista2[i+1] = min1+min2
            last = lista2[i+1]
            lista2[lastInd] = float('inf')
            suma+=last
            wyn.append([ind1,ind2])
    print(suma)
    for w in wyn:
        print(f"{w[0]+1} {w[1]+1}")