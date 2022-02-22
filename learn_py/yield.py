def fibo(n):
    a1 = 0
    a2 = 1
    yield a1
    yield a2
    
    suma = a1 + a2
    while n>a1+a2:
        suma = a1 + a2        
        yield suma
        a1= a2
        a2=suma
print(list(fibo(1234123)))