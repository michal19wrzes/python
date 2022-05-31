#Problem: https://pl.spoj.com/problems/MPOWER/

#fast exponentiation modulo
def fem(a, k, n):

    b = bin(k)[2:] # list of bits
    m = len(b)
    r = 1 # result
    x = a % n
    for i in range(m-1, -1, -1):
        if b[i] == '1':
            r = r * x % n
        x **= 2
        x  %= n
    return r

t = int(input())
for test in range(t):
    inp = input().split()
    inp = [int(x) for x in inp]
    print(fem(inp[0],inp[1],inp[2]))

# import time
# def timeChecker(func):
#   def wrapper(x,y,z):
#     n = time.time()
#     s = func(x,y,z)
    
#     print(f"Czas wykonania: {time.time()-n}")
#     return s
#   return wrapper

# def phi(n):
#   suma = n
#   dzielnik = 2
#   while (n != 1):
#     while (n % dzielnik != 0):
#       dzielnik+=1
#     suma *= (1 - 1.0 / dzielnik)
#     while (n % dzielnik == 0):
#       n /= dzielnik
#   return int(suma)

# def phi(n):
#   licznik = 0
#   for i in range(n+1):
#     if (nwd(i, n) == 1):
#       licznik+=1
  
#   return licznik

# def nwd(x,y):
#   c=1
#   while y!=0:
#     c = x%y
#     x = y
#     y = c
#   return x

# @timeChecker
# def fastPowerMod(x,y,m):
#   w = x
#   if (nwd(x,m)==1):
#     y = y%phi(m)
#   for i in range(y):
#     w = (w*x)%m
#   return w

# print(fastPowerMod(13,42,15))
# print(nwd(13,169))