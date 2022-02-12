def dodaj(list):
    sum=0
    for liczba in list:
        sum+=int(liczba)
    return sum
try:
    t = int(input())
    liczby=[]
    for i in range(t):
        x = int(input())
        liczby = input().split()
        print(dodaj(liczby))
        continue
    sys.exit(0)
except:
    pass