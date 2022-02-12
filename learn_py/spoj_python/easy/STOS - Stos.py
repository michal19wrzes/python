#STOS - Stos
#https://pl.spoj.com/problems/STOS/
try:
    lista=[]
    while True:
        n = input()
        if n == '+':
            if len(lista)>=10:
                print(':(')
                continue
            m = int(input())
            lista.append(m)
            print(':)')
        try:
            if n == '-':
                print(lista.pop())
        except:
            print(':(')
except:
    pass
        
        