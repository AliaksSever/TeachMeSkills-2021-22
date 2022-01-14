# В массиве целых чисел с количеством элементов 19 определить максимальное число
# и заменить им все четные по значению элементы.

import random


tm = [random.randint(0,20) for i in range(19)]
print(tm)

max_number = max(tm)
index = 0


while index<len(tm):
    if tm[index]%2 == 0:
        tm[index] = max_number
    index+=1
print(tm)

'''for i in range(len(tm)):
    if i%2 == 0:
        tm[i] = max_number
print(tm)'''