import numpy as np
from numpy import int64

path = input() #input filename
with open(path,'r') as file:
    count_of_elephants = int(file.readline())
    masses_of_elephants = np.array(file.readline().split(), dtype=int64)
    input_permutation = np.array(file.readline().split(), dtype=int64)
    director_permutation = np.empty(count_of_elephants, dtype=int64)

    i = 0
    for number in file.readline().split():
        director_permutation[ int(number) - 1 ] = input_permutation[i]
        i += 1

odw = [False for x in range(count_of_elephants+1)]
count_of_cycles = 0
sum_of_elephant_in_cycle =0
sums_of_cycles =[]
indices_in_cycles = []
min_vals_of_cycles=[]

for i in range(1,count_of_elephants+1):
    if not odw[i]:
        indices_in_cycle = []
        count_of_cycles +=1
        x=i
        while not odw[x]:
            odw[x]=True
            sum_of_elephant_in_cycle += masses_of_elephants[x-1]
            x = director_permutation[x-1]
            indices_in_cycle.append(x)

        sums_of_cycles.append(sum_of_elephant_in_cycle)
        indices_in_cycles.append(indices_in_cycle)
        sum_of_elephant_in_cycle =0

for i in range(count_of_cycles):
    minimum = float('inf')
    for e in indices_in_cycles[i]:
        minimum = min(minimum,masses_of_elephants[e-1])
    min_vals_of_cycles.append(minimum)

w = 0
for i in range(count_of_cycles):
    method1=sums_of_cycles[i] + (len(indices_in_cycles[i])-2) * min_vals_of_cycles[i]
    method2=sums_of_cycles[i] + min_vals_of_cycles[i] + (len(indices_in_cycles[i])+1) * min(min_vals_of_cycles)
    w += min(method1,method2)
print(w)