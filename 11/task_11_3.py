
# Задание: 3. Cоздать подтип спортивной машины который увел скорость быстрее и тормозит тоже быстрее
# Создать тип грузовой, у которой ограничение скорости 60км.
# Если пытается увеличить, должен отвечать ('не рискуйте жизнью')
# Электрокар в котором добавляется метод зарядка и уровень заряда
# если зарядка меньше 50%, ограничить скорость до 40км
# метод зарядка заряжает до 100%'''

class Car:
    def __init__(self, brand, model, year, speed = 0):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed


    # увеличить скорости
    def speed(self, speed = None):
        if not speed:
            self._speed+=5
        else:
            self._speed+=speed


    #уменьшение скорости
    def reduce_speed(self, speed = 0):
        if self._speed <= 0:
            self._speed = 0
            print('Speed is 0. Car is stopped')
        else:
            if not speed:
                if self._speed >= speed:
                    self._speed -= 5
                else:
                    self._speed = 0
                    print('Speed was reduced. Car is stopped')
            else:
                if self._speed >= speed:
                    self._speed -= speed
                else:
                    self._speed = 0
                    print('Speed was reduced. Car is stopped')


    # стоп(сброс скорости на 0)
    def stop(self):
        self._speed = 0


    # отображение скорости:
    def getspeed(self):
        print(self._speed)


    # разворот(изменение знака скорости)
    def reverse(self):
        if self._speed != 0:
            self._speed *= -1
        else:
            print('Car is stopped')





#СпортКар
class SportCar(Car):
    def speed(self, speed = None):
        if not speed:
            self._speed+=20
        else:
            self._speed+=speed


    def reduce_speed(self, speed = 0):
        if self._speed <= 0:
            self._speed = 0
            print('Speed is 0. Car is stopped')
        else:
            if not speed:
                if self._speed >= speed:
                    self._speed -= 10
                else:
                    self._speed = 0
                    print('Speed was reduced. Car is stopped')
            else:
                if self._speed >= speed:
                    self._speed -= speed
                else:
                    self._speed = 0
                    print('Speed was reduced. Car is stopped')





#Грузовик
class Truck(Car):
    def speed(self, speed = 0):
        if self._speed < 60 and speed <= 60:
            if not speed:
                self._speed+=5
            else:
                self._speed+=speed
        else:
            self._speed = 60
            print('скорость 60 км/ч, не рискуйте жизнью')





#ЭлектроКар
class ElectricCar(Car):
    charge_level = 0


    def charge(self, charge_level = 0):
        if self.charge_level < 100 and charge_level + self.charge_level <= 100:
            if not charge_level:
                self.charge_level += 15
            else:
                self.charge_level+=charge_level
        else:
            self.charge_level = 100
            print('Макс., заряд - 100%')


    def speed(self, speed = 0):
        if self.charge_level < 50:
            if self._speed < 40 and self._speed + speed <= 40:
                if not speed:
                    self._speed+=5
                else:
                    self._speed+=speed
            else:
                self._speed = 40
                print('Недостаточно заряда')
        else:
            if not speed:
                self._speed += 5
            else:
                self._speed += speed





d1 = Car('BMW', 'X6', 2006)

ds = SportCar('BMW', 'X6', 2006)
dt = Truck('КамАЗ', '43255',2003)
de = ElectricCar('Tesla', 'Model S', 2012)



