#PA05_POT - Czy umiesz potęgować
#https://pl.spoj.com/problems/PA05_POT/
D = int(input())
for test in range(D):
    n = input().split()
    podstawa = int(n[0])
    podstawa %=10
    wykladnik = int(n[1])
    if wykladnik > 0:
        if(wykladnik % 4 == 0):
            wykladnik = 4
        else:
            wykladnik = wykladnik % 4
        wynik = podstawa
        
        for i in range(wykladnik-1):
            wynik *= podstawa
        print(wynik%10)
    else:
        print(1)