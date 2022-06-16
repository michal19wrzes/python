import math
listx = [1,2,3,4,5,6,8,9]
x=8
def szukajBin(n,lista):
    l=0
    p=len(lista)-1
    
    while True:
        s= math.floor((l+p)/2)
        if lista[s]==n:
            print(f"szukana jest na {s}-tej pozycji")
            break
        elif lista[s]>n:
            p=s
        elif lista[s]<n:
            l=s
szukajBin(x,listx)
#szukana jest na 6-tej pozycji