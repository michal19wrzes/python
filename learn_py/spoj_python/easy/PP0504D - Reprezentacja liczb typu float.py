#PP0504D - Reprezentacja liczb typu float
#httpspl.spoj.comproblemsPP0504D
import struct
import re
def float_to_hex(f)
    if f == 0
        print(0 0 0 0)
    else
        c = str(hex(struct.unpack('I', struct.pack('f', f))[0]))
        c = c.replace(0x,'')
        listOfBytes = re.findall(r'.{1,2}',c)
        for i in range(len(listOfBytes))
            if listOfBytes[i][0]=='0' and listOfBytes[i][1]!='0'
                listOfBytes[i] = listOfBytes[i][1]
                continue
            if listOfBytes[i] == '00'
                listOfBytes[i] = '0' 
        print(' '.join(listOfBytes))

t = int(input())
for test in range(t)
    n = float(input())
    float_to_hex(n)

