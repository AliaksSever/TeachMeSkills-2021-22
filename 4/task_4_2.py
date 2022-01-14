spisok = list(range(int(input('Начало списка: ')),int(input('Конец списка: '))))
su = 0
index = 0

# Способ 1. С помощью While
'''
while index<len(spisok):
    if spisok[index]%2==0:
        su+=1
    index+=1
print(su)'''

# Способ 2. С помощью For
for i in spisok:
    if i%2==0:
        su+=1
print(su)






































