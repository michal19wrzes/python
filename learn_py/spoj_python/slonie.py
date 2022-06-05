#https://szkopul.edu.pl/c/oboz10-14grupa__minus1/p/slo/18246/
count_of_elephants=int(input())
masses_of_elephants = [int(x) for x in input().split()]
input_permutation = [int(x) for x in input().split()]
output_permutation = [int(x) for x in input().split()]

def p(n):
    #return key of elephant, which should be replaced with n in final permutation
    return input_permutation[output_permutation.index(n)]

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
            x = p(x)
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