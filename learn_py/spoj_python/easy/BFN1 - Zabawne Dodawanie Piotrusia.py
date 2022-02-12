#BFN1 - Zabawne Dodawanie Piotrusia
#https://pl.spoj.com/problems/BFN1/

def czyPalindrom(n):
    n = str(n)
    nlen = len(n)
    if nlen ==1:
        return True
    elif nlen%2==0:
        #even
        for nl in range(int(nlen/2)):
            if n[nl]==n[nlen-1-nl]:
                return True
            else:
                return False
    else:
        #odd
        for nl in range(round(nlen/2)-1):
            if n[nl]==n[nlen-1-nl]:
                return True
            else:
                return False
    
def lustro(a):
    a = str(a)
    b =[] 
    for i in range(len(a)):
        b.append(a[len(a)-1-i])
    return ''.join(b)


t = int(input())
for test in range(t):
    n = input()
    czyPalindrom(int(n))
    licznik = 0
    while not czyPalindrom(int(n)):
        
        licznik+=1
        x = int(lustro(n))
        n = x + int(n)
    
    print(str(n)+' '+str(licznik))
   

    
            
