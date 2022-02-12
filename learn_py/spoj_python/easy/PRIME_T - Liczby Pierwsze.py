
def czyPierwsza(num):
    flag = False
    if num>1:
        for i in range(2,num):
            if num%i==0:
                flag = True
                break
    if flag or num==1:
        return "NIE"
    else:
        return "TAK"
t = int(input())
wyniki=[]
for test in range(t):
    l = int(input())
    wyniki.append(czyPierwsza(l))
for wynik in wyniki:
    print(wynik)
    
    