import math

#print 3 sorted elements for divided len via 3 list
def splitList(l):
  x = len(l)//3
  for i in range(x):
    temp=[]
    temp.append(l[i*3])
    temp.append(l[i*3+1])
    temp.append(l[i*3+2])
    temp.sort()
    print(f"{temp[0]} {temp[1]} {temp[2]}")

t = int(input())
for test in range(t):
  cov = int(input())
  inData=[]
  dist=[]
  outData={}
  
  for v in range(cov):
    inData.append(input().split())
  for data in inData:
    maxDist=0
    for lata in inData: #
      r1 = int(lata[1])-int(data[1])
      r2 = int(lata[0])-int(data[0])
      d = math.sqrt(r1*r1+r2*r2) #distance from p to p

      if d>maxDist:
        maxDist=d
    dist.append(maxDist)    

  for i in range(len(inData)):
    outData[str(i+1)]=dist[i]
  outData = {k:v for k,v in sorted(outData.items(),key=lambda x: x[1], reverse=True)}
  splitList(list(outData.keys()))