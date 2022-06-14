import itertools
#https://pl.spoj.com/problems/TPERM2/
#Generate all permutations for entered k subsequent ascii characters
t = int(input())
for test in range(t):
  k = int(input())
  letters =[chr(x) for x in range(97,97+k)]
  [print(''.join(x)) for x in itertools.permutations(letters,len(letters))]