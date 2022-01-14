index = 0
index2 = 1
my_str = [1,1]

# Способ 1. С помощью While
'''
while True:
    su = my_str[index] + my_str[index2]
    my_str.append(su)
    index+=1
    index2+=1
    if len(my_str) == 15:
        break
print(my_str)'''


# Или 2 способ с while
n = int(input("Enter n: "))
f1 = 1
f2 = 1
'''print(f1,f2, end= ' ')'''

'''while n>2:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    n-=1'''

# Способ 2. С помощью For
print(f1,f2, end= ' ')
for i in range(2,n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')