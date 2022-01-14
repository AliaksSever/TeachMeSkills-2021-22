
def summa(a,b):
    return a+b

def dif(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(f'Делитель не может быть 0! - {err}!!!')

