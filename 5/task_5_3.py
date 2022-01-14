
lst = range(200,301)
dct = {} # словарь куда будем заносить числа (key) и суммы делителей (values)
index = 0

while index<len(lst): # нашли суммы делителей
    su = 0  # сумма делителей / ставим здесь чтобы сумма обнулялась при завершении цикла для одного числа
    d = 1  # делитель / ставим здесь чтобы индекс обнулсля (до 1) при завершении цикла
    while d<lst[index]:
        if lst[index]%d == 0:
            su+=d
        d+=1
    dct[lst[index]] = su
    index+=1
print(dct)

for key, value in dct.items():
    if dct.get(value) == key:
        print(key)