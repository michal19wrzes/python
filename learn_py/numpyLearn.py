#NUMPY
import numpy as np
lista1 = [1,3,-5,6]
a = np.array(lista1)


b = a

print(f"object: {a} typ: {type(a)} id: {id(a)}")
print(f"object: {b} typ: {type(b)} id: {id(b)}")

#+7 do kazdej z wartosci
print(a.__add__(7))

#wartosc bezwzgledna kazdej z wartosci
print(a.__abs__())

#dzieli przedzial na ,,ilosc zakresow
# print(np.linspace(5,10,3))
# [5.   7.5 10. ]

print(np.arange(2,10,2))
# [2 4 6 8]

# tablica n-wymiarowa
s = np.array([[1,2,3],[4,5,6]])

#zaplenia zerami typu int tablice 3x3
print(np.zeros((3,3),int))

#zapelnia jedynkami tablice 2x3 wiersz x kolumna
print(np.ones((2,3)))

#zapelnia tablice 2x3 randomowymi wartosciami z zakresu 0.00000000 do 1.00000000
print(np.random.random((2,3)))

#kształt tablicy to ilosc tablic w tablicy oraz ilosc wartosci w kazdej z nich
b = np.array([[6,7,8,9],[12,3,5,6]])
print(b.shape)
#(2, 4) 
# b = np.array([[6,7,8,9],[12,3]])
print(b.shape)
#(2,)

# zwraca odpowiedniki, musi byc ten sam ksztalt
print(b.T)
# [[ 6 12]
#  [ 7  3]
#  [ 8  5]
#  [ 9  6]]

# warunek, ale musi byc ten sam ksztalt
print(b%2==0)
# [[ True False  True False]
#  [ True False False  True]]


b = np.array([[6,7,8,9],[12,3,5,6]])
print(b[:2,:2])
#[[ 6  7]
#  [12  3]]

#Wszystkie wartosci z wszystkich list
print(list(b.flat))