#1
class Car:
    def __init__(self, brand, year_of_issue, mileage, speed = 0, status = 0):
        self.__brand = brand
        self.__year_of_issue = year_of_issue
        self.__mileage = mileage
        self.__speed = speed
        self.__status = status

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year_of_issue(self):
        return year_of_issue
    @year_of_issue.setter
    def year_of_issue(self, year_of_issue):
        self.__year_of_issue = year_of_issue

    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage

    def start_the_car(self):
        self.__status = 1 # двигатель заведен
        print(f'{self.brand}: is ready to ride')

    def stop_the_car(self):
        self.__status = 0 # двигатель остановлен
        print(f'{self.brand}: stopped')

    def getspeed(self):
        return self.__speed

    def setspeed(self, speed = None):
        if self.__status == 1:
            if not speed:
                self.__speed+=10
            else:
                self.__speed += speed
        else:
            print('Car is not ready to drive, please start the car!')


d1 = Car('BMW', 2001, 10000)



#2
class Plane:
    def __init__(self, brand, year_of_issue, number_of_seats):
        self.__brand = brand
        self.__year_of_issue = year_of_issue
        self.__number_of_seats = number_of_seats

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year_of_issue(self):
        return self.__year_of_issue
    @year_of_issue.setter
    def year_of_issue(self, year_of_issue):
        self.__year_of_issue = year_of_issue

    @property
    def number_of_seats(self):
        return self.__number_of_seats
    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        self.__number_of_seats = number_of_seats

    def start_the_engine(self):
        print(f'{self.brand}: is ready to fly!')

    def stop_the_engine(self):
        print(f'{self.brand}: is stopped!')



d2 = Plane('Boeing', 2005, 170)


#3
class Boat:
    def __init__(self, brand, year_of_issue, number_of_seats):
        self.__brand = brand
        self.__year_of_issue = year_of_issue
        self.__number_of_seats = number_of_seats

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def year_of_issue(self):
        return self.__year_of_issue
    @year_of_issue.setter
    def year_of_issue(self, year_of_issue):
        self.__year_of_issue = year_of_issue

    @property
    def number_of_seats(self):
        return self.__number_of_seats
    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        self.__number_of_seats = number_of_seats

    def start_the_engine(self):
        print(f'{self.brand}: is ready!!')

    def stop_the_engine(self):
        print(f'{self.brand}: is stopped!')


d3 = Boat('Bavaria', 2010, 6)


#4
class Phone:
    def __init__(self, brand, serial_number, model, status = 0):
        self.__brand = brand
        self.__serial_number = serial_number
        self.__model = model
        self.status = status

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def serial_number(self):
        return self.__serial_number
    @serial_number.setter
    def serial_number(self, serial_number):
        self.__serial_number = serial_number

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, brand):
        self.__model = model

    def turn_off(self):
        print(f'{self.brand}:{self.model} is turned off(')

    def turn_on(self):
        self.status = 1
        print(f'{self.brand}:{self.model} is turned on!')

    def ring(self):
        if self.status == 1:
            print(f'{self.brand}:{self.model} is ringing!')
        else:
            print(f'{self.brand}:{self.model} is turned off, it can not ring, please turn it on!')

d4 = Phone('iPhone', 10231231, '12mini')



#5
class Computer:
    def __init__(self, brand, serial_number, model, status = 0):
        self.__brand = brand
        self.__serial_number = serial_number
        self.__model = model
        self.status = status


    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def serial_number(self):
        return self.__serial_number
    @serial_number.setter
    def serial_number(self, serial_number):
        self.__serial_number = serial_number

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, brand):
        self.__model = model

    def turn_off(self):
        if self.status == 0:
            print(f'{self.brand}:{self.model} is already turned off!')
        else:
            self.status = 0
            print(f'{self.brand}:{self.model} is turned off(')

    def turn_on(self):
        self.status = 1
        print(f'{self.brand}:{self.model} is turned on!')

    def unlock_screen(self):
        if self.status == 1:
            for i in range(3):
                password = int(input('please, enter password: '))
                if password == 123456:
                    print(f'{self.brand}:{self.model} is ready for work!')
                    break
                else:
                    print(f'{self.brand}:{self.model} password is incorrect, please try again!')
        else:
            print(f'{self.brand}:{self.model} is turned off, please turn it on!')



d5 = Computer('Apple', 123132814, 'MacBook Air')

