
# Задание: Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы:
# переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
# Реализовать нормальное отображение времени(не 12:65:83 а  - 13:06:23)

class MyTime:
    # Конструктор:
    def __init__(self, hours=None, minutes=None, seconds=None):
        if type(hours) == type(minutes) == type(seconds) == int:
            self._hours = hours
            self._minutes = minutes
            self._seconds = seconds
        elif type(hours) == str:
            tmp = hours.split(":")
            self._hours = int(tmp[0])
            self._minutes = int(tmp[1])
            self._seconds = int(tmp[2])
        elif isinstance(hours, MyTime):
            self._hours = hours._hours
            self._minutes = hours._minutes
            self._seconds = hours._seconds
        elif hours == minutes == seconds is None:
            self._hours = 0
            self._seconds = 0
            self._minutes = 0

    # Методы:
    def Print(self):
        if self._seconds > 60:
            k = self._seconds % 60 # отсаток удет в секунды
            c = self._seconds // 60 # целая часть, пойдет в минуты
            self._seconds = k
            self._minutes += c
        if self._minutes > 60:
            k = self._minutes % 60 # отсаток удет в минуты
            c = self._minutes // 60 # целая часть, пойдет в часы
            self._minutes = k
            self._hours += c
        if self._hours > 24:
            k = self._hours % 24 # остаток и есть текущий час, после 24 идет обнуление
            c = self._hours // 24
            self._hours = k
        print(f"{self._hours}:{self._minutes}:{self._seconds}")

    def __eq__(self, other):  # ==
        return self._hours == other._hours and self._minutes == other._minutes and self._seconds == other._seconds

    def __ne__(self, other):  # !=
        return self._hours != other._hours or self._minutes != other._minutes or self._seconds != other._seconds

    def __ge__(self, other):  # >=
        return ((self._hours * 60 + self._minutes) + self._seconds / 60) >= (
                (other._hours * 60 + other._minutes) + other._seconds / 60)

    def __le__(self, other):  # <=
        return ((self._hours * 60 + self._minutes) + self._seconds / 60) <= (
                (other._hours * 60 + other._minutes) + other._seconds / 60)

    def __gt__(self, other):  # >
        return ((self._hours * 60 + self._minutes) + self._seconds / 60) > (
                (other._hours * 60 + other._minutes) + other._seconds / 60)

    def __lt__(self, other):  # <
        return ((self._hours * 60 + self._minutes) + self._seconds / 60) < (
                (other._hours * 60 + other._minutes) + other._seconds / 60)

    def __add__(self, other): # Сложение
        time = MyTime()
        time._hours = self._hours + other._hours
        time._minutes = self._minutes + other._minutes
        time._seconds = self._seconds + other._seconds
        time.Print()

    def __sub__(self, other): # Вычитание
        time = MyTime()
        time._hours = abs(self._hours - other._hours)
        time._minutes = abs(self._minutes - other._minutes)
        time._seconds = abs(self._seconds - other._seconds)
        time.Print()

    def __mul__(self, other): # Умножение
        time = MyTime()
        time._hours = self._hours * other
        time._minutes = self._minutes * other
        time._seconds = self._seconds * other
        time.Print()


def main():
    r = MyTime('30:5:105')
    s = MyTime(1, 10, 45)
    r.Print()
    s.Print()
    print(r == s)
    print(r != s)
    print(r >= s)
    print(r <= s)
    print(r > s)
    print(r < s)
    r + s
    r - s
    r * 1



if __name__ == '__main__':
    main()