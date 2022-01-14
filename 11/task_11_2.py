
# Задание: Создать класс Car.
# Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0),
# отображение скорости,
# разворот(изменение знака скорости).
# Все атрибуты приватные.

class Car:
    def __init__(self, brand, model, year, speed = 0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed


    # увеличить скорости
    def speed(self, speed = None):
        if not speed:
            self.__speed+=5
            #print(f'speed is {self.__speed} km / h')
        else:
            self.__speed+=speed
            #print(f'speed is {self.__speed} km / h')


    #уменьшение скорости
    def reduce_speed(self, speed = 0):
        if self.__speed <= 0:
            self.__speed = 0
            print('Speed is 0. Car is stopped')
        else:
            if not speed:
                if self.__speed >= speed:
                    self.__speed -= 5
                else:
                    self.__speed = 0
                    print('Speed was reduced. Car is stopped')
            else:
                if self.__speed >= speed:
                    self.__speed -= speed
                else:
                    self.__speed = 0
                    print('Speed was reduced. Car is stopped')

    # стоп(сброс скорости на 0)
    def stop(self):
        self.__speed = 0

    # отображение скорости:
    def getspeed(self):
        print(self.__speed)

    # разворот(изменение знака скорости)
    def reverse(self):
        if self.__speed != 0:
            self.__speed *= -1
        else:
            print('Car is stopped')


d1 = Car('BMW', 'X6', 2006)


