spisok = list(range(int(input('Начало списка: ')),int(input('Конец списка: '))))
index = 0

# Способ 1. С помощью While
'''
while index < len(spisok):
    spisok[index]*=-2
    index+=1
print(spisok)'''

# Способ 2. С помощью For

for i in range(len(spisok)):
    spisok[i]*=-2
print(spisok)




























