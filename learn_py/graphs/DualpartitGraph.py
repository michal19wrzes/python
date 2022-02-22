##Program podaje stopien grafu wczesniej wpisanego na zasadzie ³¹czeñ wierzcho³ków poprzez krawêdzie,
##Uzytkownik wpisuje numer wierzcholka, nastepnie numer wierzcholka polaczonego z nim krawêdzi¹
##Podanie ujemnej wartosci dla wspolrzednej powoduje zakonczenie programu.
def dfs(Graf, start):
    """Sprawdzenie spojnosci grafu poprzez DFS G- wczytanie grafu, start- wierzcholek rozpoczecia"""
    visited=[False]*len(Graf[0])
    lista_pom = []
    stack=[]
    stack.append(start)
    while len(stack)!=0:
        v=stack.pop()
        if visited[v]==False:
            visited[v]=True
            print(v+1)
            lista_pom.append(v+1)
            print lista_pom
            for w in range(len(Graf[0])):
                if Graf[v][w]!=0:
                    stack.append(w)
    return lista_pom


def bfs(Graf, start):
        path = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in path:
                path.append(vertex+1)
                print 'path : ',path
                queue.extend(Graf[vertex])
                print 'queue : ',queue
        return path
##zeby algorytm dzialal wywolaj bfs(Graf,0):



n = input("Wprowadz ilosc wierzcholkow w grafie [bok kwadratowej tablicy] :")
deg = []
for c in range(1,n+1):
    deg.append(0)
from numpy import*
tab=zeros((n,n),int)
print tab







while True:
    a = input("Wska¿ wierzcho³ek(wiersz) :")
    if a<1:
        break
    if a>n:
        print'bledna wartosc'
        continue
    
    b = input("wska¿ po³¹czenie z wierzcho³kiem(kolumna) :")
    if b>n:
        print'bledna wartosc'
        continue
    tab[a-1][b-1]+=1
    tab[b-1][a-1]+=1
    print tab
   
    
for i in range(0,n):
    for e in range(0,n):
        deg[e-1]+=tab[i-1][e-1]
deg.sort()
deg.reverse()
print 'Ci¹g stopni to =',deg
print 'Stopien grafu to deg =',deg[0]
print 'Przebieg BFS:',bfs(tab,0)
print 'Przebieg DFS:'

lista_pom = dfs(tab, 0)

##WARUNEK GRAFU NIESPOJNEGO
for i in range(0,n):
    if deg[i] == 0 or len(lista_pom)!=n:
        print 'Graf jest niespojny'
        break
    
##SPRAWDZANIE PARZYSTOSCI STOPNI W GRAFIE
nieparzysta = False
parzysta = True
for i in range(0,n):
    if deg[i]%2 ==0:
        parzysta = True
    else:
        nieparzysta = True
##WARUNEK GRAFU EULEROWSKIEGO
if parzysta == True and nieparzysta == False and len(lista_pom)==n:
    print 'Graf jest eulerowski'
    euler = True

##WARUNEK GRAFU POLEULEROWSKIEGO
nieparzysta1 = 0
for i in range(0,n):
    if deg[i]%2 ==0:
        parzysta = True
    else:
        nieparzysta1+=1
if nieparzysta1 == 1 or 2 and len(lista_pom)==n:
    print'Graf jest poleulerowski'






