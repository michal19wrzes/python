import math

#print 1 2 6 3 4 5  for exampleList:[1,6,2,5,3,4] --> sort after 3 numbers
def splitList(l):
  x = len(l)//3
  for i in range(x):
    temp=[]
    temp.append(l[i*3])
    temp.append(l[i*3+1])
    temp.append(l[i*3+2])
    temp.sort()
    print(f"{temp[0]} {temp[1]} {temp[2]}")

#input test case. for. ex. 1
t = int(input())
inData=[] # input Data
maxDists=[]   # maximal distances between two points
outData={} # output data
for test in range(t):
  cov = int(input()) # cov - count of vertices
  for v in range(cov):
    inData.append(input().split()) # inputData for. Ex. 0 0 \n 1 2 \n 2 1

  #calc maxDistance from vertex1 to vertex2 for vertices
  for data in inData:
    maxDist=0
    for lata in inData: #
      r1 = int(lata[1])-int(data[1])
      r2 = int(lata[0])-int(data[0])
      d = math.sqrt(r1*r1+r2*r2) #distance from p to p

      if d>maxDist: #looking for a greatest distance
        maxDist=d
    maxDists.append(maxDist)    

#create dict with index and maxDistances before sorting
  for i in range(len(inData)):
    outData[str(i+1)]=maxDists[i]

  #sorting dict by value
  outData = {k:v for k,v in sorted(outData.items(),key=lambda x: x[1], reverse=True)}

  #print 1 2 6 3 4 5  for exampleList:[1,6,2,5,3,4] --> sort after 3 numbers
  splitList(list(outData.keys()))