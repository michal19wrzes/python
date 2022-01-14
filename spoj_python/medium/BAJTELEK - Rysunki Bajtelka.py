#BAJTELEK - Rysunki Bajtelka
#https://pl.spoj.com/problems/BAJTELEK/
def pole(lista):
    suma = 0
    xs = []
    ys = []
    for i in range(0,len(lista),2):
        xs.append(lista[i])
    for p in range(1,len(lista),2):
        ys.append(lista[p])
    for f in range(len(xs)):
        if f != len(xs)-1:
            suma += (float(xs[f+1])+float(xs[f]))*(float(ys[f+1])-float(ys[f]))   
    return suma/2
    
    
t = int(input())
wyniki=[]
for test in range(t):
    black = input().split()
    gray = input().split()
    b = pole(black)
    black_value = b*10
    g = pole(gray)
    gray_value = (g-b)*6
    wyniki.append(int(black_value+gray_value))
    print()
for wynik in wyniki:
    print(wynik)
    
    