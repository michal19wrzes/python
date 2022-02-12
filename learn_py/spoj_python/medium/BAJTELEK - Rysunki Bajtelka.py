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
    return abs(suma)/2
    
    
t = int(input())
wyniki=[]
for test in range(t):
    first = input().split()
    second = input().split()
    if len(first) > len(second):
        g = pole(first)
        b = pole(second)    
        black_value = b*10
        gray_value = (g-b)*6       
        wyniki.append(int(black_value+gray_value))
        print()
        
    else:
        b = pole(first)
        g = pole(second)
        black_value = b*10
        gray_value = (g-b)*6
        wyniki.append(int(black_value+gray_value))
        print()
     
for wynik in wyniki:
    print(wynik)
    
    