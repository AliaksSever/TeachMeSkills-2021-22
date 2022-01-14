# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

spisok = [1,2,3,4,5]
index = 0

# Способ 1. С помощью While

'''while index<len(spisok): # или While True:
    spisok.append(spisok[0])
    spisok.pop(0)
    break
print(spisok)'''

# Способ 2. С помощью For

for i in spisok:
    spisok.append(spisok[0])
    spisok.pop(0)
    break
print(spisok)