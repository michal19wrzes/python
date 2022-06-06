import numpy as np
import fileinput
from numpy import int64

ins = list(fileinput.input())
count_of_elephants = int(ins[0])
masses_of_elephants = np.array(ins[1].split(), dtype=int64)
min_weight = min(masses_of_elephants)
input_permutation = np.array(ins[2].split(), dtype=int64)
director_permutation = np.empty(count_of_elephants, dtype=int64)

i = 0
for number in ins[3].split():
    director_permutation[ int(number) - 1 ] = input_permutation[i]
    i += 1

odw = [False for x in range(count_of_elephants+1)]
score = 0
for i in range(1,count_of_elephants):
    if not odw[i]:
        weights_of_elephtants = 0
        length_of_cycle = 0
        min_of_cycle = float('inf')
        x=i
        while not odw[x]:
            odw[x]=True
            weights_of_elephtants += masses_of_elephants[x-1]
            x = director_permutation[x-1]
            min_of_cycle = min(min_of_cycle,masses_of_elephants[x-1])
            length_of_cycle += 1
        score += min(weights_of_elephtants + (length_of_cycle - 2) * min_of_cycle,
                     weights_of_elephtants + min_of_cycle + (length_of_cycle + 1) * min_weight)
print(score, end='')