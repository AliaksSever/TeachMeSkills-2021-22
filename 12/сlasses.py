
import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Figure:
    def perimetr(self):
        pass
    def area(self):
        pass


class Circle(Point, Figure):
    def __init__(self, x,y,r):
        super().__init__(x,y)
        self._r = r

    def perimetr(self):
        result = 2*math.pi*self._r
        return result

    def area(self):
        resutl = math.pi*self._r**2
        return resutl


class Triangle(Point, Figure):
    def __init__(self, x,y,z):
        super().__init__(x,y)
        self._z = z

    def perimetr(self):
        rusult = self._x + self._y + self._z
        return rusult

    def area(self):
        p = self.perimetr()/2
        result = math.sqrt(p*(p - self._x)*(p - self._y)*(p - self._z))
        return result


class Square(Point, Figure):
    def perimetr(self):
        result = (self._x + self._y)*2
        return result
    def area(self):
        result = self._x*self._y
        return result
