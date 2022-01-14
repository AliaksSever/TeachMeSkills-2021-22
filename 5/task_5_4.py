
n = int(input('Enter n: '))

d = 0
s = 1

for i in range(2,n+1):
    d = 1/i
    s+=d
print(s)