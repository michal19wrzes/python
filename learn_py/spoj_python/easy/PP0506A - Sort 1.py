#Problem: https://pl.spoj.com/problems/PP0506A/
#need fix
import math

def calcDistance(v):
    r1, r2 = 0 - v[0], 0 - v[1]
    d = round(math.sqrt(r1*r1+r2*r2),4)
    return d
    
t = int(input())

for test in range(t):
    inputData={}
    outputData={}
    cov = int(input())

    for v in range(cov):
        inp = input().split()
        inputData[inp[0]]=[int(inp[1]),int(inp[2])]
        d = calcDistance(inputData.get(inp[0]))
        outputData[inp[0]]=d
    
    outputData = {k:v for k,v in sorted(outputData.items(),key=lambda item: item[1])}
    for k in outputData.keys():
        print(f"{k} {inputData.get(k)[0]} {inputData.get(k)[1]}")
    print()