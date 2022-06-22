#NZEC FAIL - best my solution
import numpy as np
t = int(input())
for test in range(t):
    n = int(input())
    nd = [40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16,40,18,15,17,16]
    #nd = np.array(input().split(),int)
    nds = [x for x in sorted(nd)]
    ndsx = [x for x,y in sorted(enumerate(nd), key=lambda y: y[1])]
    suma = 0
    wyn = []
    for i in range(n-1):
      
      min1 = min(nds[:(i+1)*2])
      ind1 = nds.index(min1)
      nds[ind1] = float('inf')
      
      min2 = min(nds[:(i+1)*2])
      ind2 = nds.index(min2)
      nds[ind2] = float('inf')
      suma+=min1+min2
      
      if ndsx[ind1]<ndsx[ind2]:
        nds[ind1] = min1+min2
        wyn.append([ndsx[ind1],ndsx[ind2]])
      else:
        nds[ind2] = min1+min2
        wyn.append([ndsx[ind2],ndsx[ind1]])
print(suma)
[print(f"{x[0]+1} {x[1]+1}") for x in wyn]