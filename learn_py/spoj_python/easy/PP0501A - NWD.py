def nwd(a,b):
    if b>0: 
        return nwd(b,a%b)
    else:
        return a

t = int(input())
wyniki=[]

for i in range(t):
    k= []
    k = input().split() #lista wejsc
    a = nwd(int(k[0]),int(k[1]))
    wyniki.append(a)
    
for wynik in wyniki:
    print(wynik)