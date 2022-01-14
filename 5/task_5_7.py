
import random

n = int(input('Enter n:'))
m = int(input('Enter m:'))

mat = [[random.randint(1,20) for x in range(m)] for i in range(n) ]

for i in mat:
    print(i)

for i in range(4):
    for j in range(i,i+1):
        mx = max(mat[i])
        mat[i][j] = mx
#print(mat)

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=' ')
    print()