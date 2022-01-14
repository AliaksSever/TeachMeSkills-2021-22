
# Задание: Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

'''def nechetnye_chisla(func):
    def wrapper(n):
        lst = list(filter(lambda x: x%2!=0, range(1,n)))
        result = func(n)
        print(lst)
        return result
    return wrapper

@nechetnye_chisla
def my_func(n):
    list = []
    for i in range(1,n):
        list.append(i)
    return list


print(my_func(10))'''

def nechetnye_chisla(funk):
    def wrapper(*args):
        lst = list(filter(lambda x: x%2!=0, args))
        #result = funk(*args)
        #print(lst)
        return lst
        #return result
    return wrapper



@nechetnye_chisla
def my_func(*args):
    list = []
    for i in args:
        list.append(i)
    return list

print(my_func(1,2,3,4,5,6,7,8,9,10))
