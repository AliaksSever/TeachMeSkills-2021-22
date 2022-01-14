import random

class Matrix:
    data = None
    n = None
    m = None

    def __init__(self,n =5,m=5,a=0,b=0):
        if (n is None and m is None) or (m is None and b is None):
            self.data = [[0 for i in range(5)] for i in range(5)]
        else:
            self.m = m
            self.n = n
            self.a = a
            self.b = b
            self.data = [[random.randint(self.a,self.b) for j in range(self.n)] for i in range(self.m)]

    def __str__(self):
        string = ''
        for i in self.data:
            for j in i:
                string+=f'{j}  '
            string+='\n'
        return string