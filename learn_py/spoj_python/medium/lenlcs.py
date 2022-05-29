#https://pl.spoj.com/problems/LENLCS/

A = "deskorolka"
B = "stokrotka"

db = [[0 for b in range(len(B)+1)] for a in range(len(A)+1)]

for a in range(len(A)):
    prev_row = db[a]
    curr_row = db[a+1]
    a_char = A[a]
    for b in range(len(B)):
        b_char = B[b]
        if a_char == b_char:
            curr_row[b+1] = prev_row[b]+1
            continue
        curr_row[b+1] = max(curr_row[b], prev_row[b+1])

a = len(A)
b = len(B)
wynik = []

while a > 0 and b > 0:
    a_char = A[a-1]
    b_char = B[b-1]
    if a_char == b_char:
        a -= 1
        b -= 1
        wynik.append(a_char)
        continue
    if db[a-1][b] > db[a][b-1]:
        a -= 1
        continue
    b -= 1

print ("".join([str(a) for a in wynik[::-1]]))