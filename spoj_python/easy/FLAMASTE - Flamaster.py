#FLAMASTE - Flamaster
#https://pl.spoj.com/problems/FLAMASTE/
t = int(input())

liczniki=[]
for test in range(t):
    wyniki=[]
    litery =input()+'.'
    poprzednia = '.'
    licznik =1
    
    for i in range(len(litery)):
        if litery[i]!=poprzednia and poprzednia!='.':
            if licznik == 2:
                wyniki.append(poprzednia+poprzednia)
            elif licznik ==1:
                wyniki.append(poprzednia)
            elif licznik > 2:
                wyniki.append(poprzednia+str(licznik))
            liczniki.append(licznik)
            poprzednia = litery[i]
            licznik =1
        elif poprzednia == '.':
                poprzednia = litery[i]
        else:
            licznik+=1
            
    print(''.join(wyniki))

        
    