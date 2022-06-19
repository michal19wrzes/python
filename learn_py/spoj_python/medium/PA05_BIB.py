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