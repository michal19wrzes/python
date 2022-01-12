#PTROL - ROL
#https://pl.spoj.com/problems/PTROL/
def przesun(a):
    a.reverse()
    b = a.pop()
    a.reverse()
    a.append(b)
    return a


t = int(input())
for i in range(t):
    n = input().split()
    n.reverse()
    n.pop()
    n.reverse()
    print(' '.join(list(przesun(n))))
        
    