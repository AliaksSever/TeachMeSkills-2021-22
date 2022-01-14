
# 1 Написать 12 функций по переводу:

#1.Дюймы в сантиметры
def d_to_cm(d):
    cm = d*2.54
    rusult = f'{d} дюймов это {cm} сантиметров'
    return rusult

#print(d_to_cm(1))


#2.Сантиметры в дюймы
def cm_to_d(cm):
    d = cm/2.54
    return d

#print(cm_to_d(10))


#3.Мили в километры
def miles_to_km(miles):
    km = miles*1.609
    return km

#print(miles_to_km(1))


#4.Километры в мили
def km_to_miles(km):
    miles = km/1.609
    return miles

#print(km_to_miles(1))


#5.Фунты в килограммы
def f_to_kg(f):
    kg = f/2.205
    return kg

#print(f_to_kg(1))


#6.Килограммы в фунты
def kg_to_f(kg):
    f = kg*2.205
    return f

#print(kg_to_f(1))


#7.Унции в граммы
def oz_to_gr(oz):
    gr = oz/28.35
    return gr

#print(oz_to_gr(1))


#8.Граммы в унции
def gr_to_oz(gr):
    oz = gr*28.35
    return oz

#print(gr_to_oz(1))


#9.Галлон в литры
def gal_to_l(gal):
    l = gal*3.785
    return l

#print(gal_to_l(1))


#10.Литры в галлоны
def l_to_gal(l):
    gal = l/3.785
    return gal

#print(l_to_gal(1))


#12.Пинты в литры
def pt_to_l(pt):
    l = pt/2.113
    return l

#print(pt_to_l(1))


#12.Литры в пинты
def l_to_pt(l):
    pt = l*2.113
    return pt

#print(l_to_pt(1))



# Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

while True:
    v = int(input('Введите число от 1 до 12(Категория конвертирования): '))
    if v<0 or v>12:
        print('Введите число из указанного диапазона')
    elif v == 1:
        n = int(input('Введите численное значение: '))
        print(d_to_cm(n))
    elif v == 2:
        n = int(input('Введите численное значение: '))
        print(cm_to_d(n))
    elif v == 3:
        n = int(input('Введите численное значение: '))
        print(miles_to_km(n))
    elif v == 4:
        n = int(input('Введите численное значение: '))
        print(km_to_miles(n))
    elif v == 5:
        n = int(input('Введите численное значение: '))
        print(f_to_kg(n))
    elif v == 6:
        n = int(input('Введите численное значение: '))
        print(kg_to_f(n))
    elif v == 7:
        n = int(input('Введите численное значение: '))
        print(oz_to_gr(n))
    elif v == 8:
        n = int(input('Введите численное значение: '))
        print(gr_to_oz(n))
    elif v == 9:
        n = int(input('Введите численное значение: '))
        print(gal_to_l(n))
    elif v == 10:
        n = int(input('Введите численное значение: '))
        print(l_to_gal(n))
    elif v == 11:
        n = int(input('Введите численное значение: '))
        print(pt_to_l(n))
    elif v == 12:
        n = int(input('Введите численное значение: '))
        print(l_to_pt(n))
    else:
        break