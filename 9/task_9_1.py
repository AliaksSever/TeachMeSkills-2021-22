
# Задание: Дан список строк.
# Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

spisok = ['alex','name','oleg','mashina']
spisok2 = ['slovo','slovo2','slovo3']

'''def my_funk(spisok):
    list = []
    for i,val in enumerate(spisok):
        arg = f'{i+1} - {val}'
        list.append(arg)
    print(list)
my_funk(spisok)'''

my_funk = lambda spisok: print([(f'{i+1} - {value}') for i,value in enumerate(spisok)])
my_funk(spisok)