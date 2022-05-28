import math

t = int(input("T:"))
for test in range(t):
  cov = int(input("cov:"))
  inData=[]
  odl=[]
  
  for v in range(cov):
    inData.append(input(f"v{v}:").split())
    print(inData[v])

  for data in inData:
    staraOdl=0
    print(data)
    for lata in inData:
      
      r1 = int(lata[1])-int(data[1])
      r2 = int(lata[0])-int(data[0])
      
      d = math.sqrt(r1*r1+r2*r2)
      print(f"odleglosc: {data} od: {lata} to: {d}")
      if d>staraOdl:
        staraOdl=d
        
      odl.append(d)
    print(f"maxOdl:{staraOdl}")
