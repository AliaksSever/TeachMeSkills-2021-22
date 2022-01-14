
n = int(input('Начало промежутка: '))
m = int(input('Конец промежутка: '))

ls = range(n,m)

index = 0
tm = [] # для сбора делителей
dct = {} # словарь для числа и его делитей


while index<len(ls):
    d = 2
    tm = []
    while d<ls[index]:
        if ls[index]%d == 0 and ls[index] != d:
            tm.append(d)
        d+=1
        dct[ls[index]] = tm
    index+=1


for key, value in dct.items():
    if value == []:
        value = 0
    print(f'{key}: {value}')