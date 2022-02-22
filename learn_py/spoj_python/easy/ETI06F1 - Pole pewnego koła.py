#ETI06F1 - Pole pewnego koła
#https://pl.spoj.com/problems/ETI06F1/
import cmath

def circleArea(r,d):
    pi = 3.141592654
    h = cmath.sqrt(r**2-(d/2)**2)
    #f"{h if h.imag else h.real:.2f}"
    x = round((h.real**2)*pi,2)
    return x
    
    
    
n = input().split()
print(circleArea(float(n[0]),float(n[1])))


