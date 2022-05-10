def silnia(n):
    if n>1:
        return n*silnia(n-1)
    else:
        return 1
def comb(n,k):
    return silnia(n)/(silnia(k)*silnia(n-k))
    
    
def czyParzysta(n):
    return n%2==0

# print(silnia(10)) //328800
# print(comb(10,0)) //1.0
# print(czyParzysta(3628800)) //N

d = int(input())
for test in range(d):
    nk = input().split()
    if(int(nk[0])>int(nk[1])):
        n = int(nk[0])
        k = int(nk[1])
        v = comb(n,k)
        print('P' if czyParzysta(v) else 'N')
    else:
        n = int(nk[1])
        k = int(nk[0])
        v = comb(n,k)
        print('P' if czyParzysta(v) else 'N')
        
    
    

    
