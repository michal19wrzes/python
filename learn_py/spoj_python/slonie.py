#https://www.oi.edu.pl/old/html/zadania/oi16/slo.pdf
import numpy as np
import fileinput
from numpy import int64

ins = list(fileinput.input()) # zczytywanie linii pliku do listy linii
count_of_elephants = int(ins[0]) # pierwsza linia to liczba sloni
masses_of_elephants = np.array(ins[1].split(), dtype=int64) # druga linia to lista mas sloni
min_weight = min(masses_of_elephants) # minimalna waga sloni z listy sloni
input_permutation = np.array(ins[2].split(), dtype=int64) # początkowa kolejnosc sloni przed wizytą dyrektora
director_permutation = np.empty(count_of_elephants, dtype=int64) #lista pusta z przygotowanym dostępem do uzupełniania jej permutacją

i = 0
for number in ins[3].split(): # 4 linia tekstu to docelowe ustawienie dyrektora, czyli 'b'. ..dla kazdego slonia z ustawienia dyrektora
    director_permutation[ int(number) - 1 ] = input_permutation[i] # Wykonuj p[bi]=ai
    i += 1
#director_permutation to lista nazw sloni z ktorymi powinien zamienic sie slon z początkowej pozycji ze sloniem finalnej permutacji dyrektora,
#czyli jesli mamy listę director_permutation = [2,5,4,3,1,6] to slon o nazwie indeksu liczby stojącej na i-tej pozycji powinien zamienic się z wartością listy od podanego indeksu
#dla przykładu na 0 pozycji stoi 2, czyli pierwszy, czyli(0+1) slon powinien zamienić się z drugim, a na 5 pozycji licząc od 0 jest 6 więc 5+1 slon powinien zamienic się z 6 pierwotnego ustawienia

odw = [False for x in range(count_of_elephants+1)] #Zapelnienie listy falsami, by móc reprezentować odwiedzenie danego wierzchołka
score = 0 #wynik bedzie zwiekszany o masę odwiedzonych sloni
for i in range(1,count_of_elephants): #wykonuj dla kolejnych nazw sloni
    if not odw[i]: # jesli nie odwiedzony wierzcholek grafu, czyli slon
        weights_of_elephtants = 0 # laczna masa odwiedzonych sloni
        length_of_cycle = 0 # dlugosc cyklu
        min_of_cycle = float('inf') # szukana najmniejsza masa danego cyklu, początkowo +nieskonczonosc
        x=i
        while not odw[x]: # wykonuj dopoki wierzcholek jest nieodwiedzony 
            odw[x]=True # oznacz wierzcholek jako odwiedzony
            weights_of_elephtants += masses_of_elephants[x-1] # do aktualnej lacznej masy sloni dodaj masę aktualnie analizowanego slonia
            x = director_permutation[x-1] # do zmiennej x przypisz nazwę slonia z ktorym powinien zamienic się slon o nazwie x, do x zostanie przypisana nazwa slonia numerując od 1
            min_of_cycle = min(min_of_cycle,masses_of_elephants[x-1]) # szukanie minimalnej masy slonia w cyklu, wybieraj najmniejszą z dotychczas najmniejszej i masy slonia do zamiany z sloniem i
            length_of_cycle += 1 #dlugosc aktualnego cyklu +1
        #gotowe szukane zmiene by moc wyznaczyc wynik za pomocą 2 metod
        score += min(weights_of_elephtants + (length_of_cycle - 2) * min_of_cycle,
                     weights_of_elephtants + min_of_cycle + (length_of_cycle + 1) * min_weight) #wybor korzystniejszej z dwoch metod opisanych w tresci zadania
print(score, end='')