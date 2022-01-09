#PP0504B - StringMerge
#https://pl.spoj.com/problems/PP0504B/
t= int(input())
def joinWords(a,b):
    zlaczonyTekst=[]
    if len(b)<len(a):
        for i in range(len(b)):
            zlaczonyTekst.append(a[i])
            zlaczonyTekst.append(b[i])
    else:
        for i in range(len(a)):
            zlaczonyTekst.append(a[i])
            zlaczonyTekst.append(b[i])
    return (''.join(zlaczonyTekst))
    

for test in range(t):
    
    n = input().split()
    print(joinWords(n[0],n[1]))
    