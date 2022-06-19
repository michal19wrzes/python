#https://pl.spoj.com/problems/PP0506A/

t= int(input())
for test in range(t):
  n = int(input())
  inputData=[]
  for p in range(n):
    inputData.append(input().split())
  [print(' '.join(x)) for x in sorted(inputData,key=lambda x: int(x[1])**2+int(x[2])**2)]
  if test!=t-1:
    print()