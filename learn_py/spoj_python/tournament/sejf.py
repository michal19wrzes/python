import numpy as np
#https://szkopul.edu.pl/problemset/problem/Plha_6BH8_14ZptrZOdschts/site/?key=statement
#SEJF - Olimpiada inf. 
def changeRows(lista,a,b):
    lista[a],lista[b] = lista[b],lista[a]
    return lista
def changeColumns(lista,a,b):
    for row in lista:
        row[a],row[b] = row[b],row[a]
    return lista
def selectValInAB(lista,a,b):
    return int(lista[a][b])


inpNM = np.array(input().split(),int)
n = inpNM[0]
m = inpNM[1]
wyn = []
inpNM = [[(i-1)*n+j for j in range(1,n+1)] for i in range(1,n+1)]

for move in range(m):
    inp = input().split()
    if inp[0]=='P':
        wyn.append(selectValInAB(inpNM,int(inp[1])-1,int(inp[2])-1))
    elif inp[0]=='W':
        inpNM = (changeRows(inpNM,int(inp[1])-1,int(inp[2])-1))
    elif inp[0]=='K':
        inpNM = changeColumns(inpNM,int(inp[1])-1,int(inp[2])-1)
 
[print(w) for w in wyn]