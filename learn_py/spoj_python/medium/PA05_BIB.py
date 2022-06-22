#https://pl.spoj.com/problems/PA05_BIB/
import numpy as np
t = int(input())							#list of tests
for test in range(t):
    n = int(input()) 						#count of files
    nd = np.array(input().split(),int) 		#files
    nds = [x for x in sorted(nd)] 			#files sorted
    ndsx = [x for x,y in sorted(enumerate(nd), key=lambda y: y[1])] #indexes of files after sorted
    suma = 0
    wyn = [] 	#scores
    for i in range(n-1):
      
      min1 = min(nds[:(i+1)*2]) 	#minimal val of sorted list with files 
      ind1 = nds.index(min1) 		#index to min1
      nds[ind1] = float('inf')		#visited change to infinity
      
      min2 = min(nds[:(i+1)*2])		#minimal val of sorted list with files
      ind2 = nds.index(min2)		#index to min2
      nds[ind2] = float('inf')		#visited change to infinity

      suma+=min1+min2				#cost of merging files
      
      if ndsx[ind1]<ndsx[ind2]:		# ndsx[ind1] will be left value of comparing values
        nds[ind1] = min1+min2		# set sum of comparing values to left value
        wyn.append([ndsx[ind1],ndsx[ind2]])
      else:							# ndsx[ind2] will be left value of comparing values
        nds[ind2] = min1+min2 		# set sum of comparing values to left value
        wyn.append([ndsx[ind2],ndsx[ind1]])
print(suma) 						#time need to merging files 
[print(f"{x[0]+1} {x[1]+1}") for x in wyn] #indexes of files that will be merging
