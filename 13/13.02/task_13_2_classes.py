
class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def summa(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        try:
            return self.a/self.b
        except ZeroDivisionError as err:
            print(f'Делитель не может быть 0! - {err}!!!')

