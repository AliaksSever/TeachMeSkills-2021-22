# Создать список поездов.
# Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со
# временем в Python(библиотека datetime)

# 1. создать списко словарей [{'номер поезда': пункт прибытия, 'время': , 'пункт: , 'время отбытия': },
#                              {},
#                              {},
#                              {}]

import datetime


lst_of_dct =[{'train number':32,'arrival place':'Moscow','arrival time':'23:55:00' ,'departure time':'18:45:00' ,'departure place':'Minsk'},
             {'train number':31,'arrival place':'Minsk','arrival time':'18:30:00' ,'departure time':'15:00:00' ,'departure place':'Grodno'},
             {'train number':30,'arrival place':'Moscow','arrival time':'22:00:00' ,'departure time':'15:00:00' ,'departure place':'Piter'},
             {'train number':28,'arrival place':'Gomel','arrival time':'20:45:00' ,'departure time':'12:30:00' ,'departure place':'Brest'},
             {'train number':29,'arrival place':'Mogilev','arrival time':'19:30:00' ,'departure time':'16:30:00' ,'departure place':'Vitebsk'}]


for i in lst_of_dct:
    tdelta = datetime.datetime.strptime(i['arrival time'], '%H:%M:%S') - datetime.datetime.strptime(i['departure time'], '%H:%M:%S')
    d = datetime.datetime.strptime('07:20:00', '%H:%M:%S') - datetime.datetime.strptime('00:00:00', '%H:%M:%S') # переменная в которой находиться значение 7:20:00
    if tdelta>d: # не нашел другой способ как сравнить tdelta(типа timedelta) со значение 7:20:20
        print(i)