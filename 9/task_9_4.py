
# Задание: Создать универсальный декоратор,
# который меняет порядок аргументов в функции на противоположный.

def my_dec(func):
    def wrapper(*args):
        #lst = list(args[::-1])
        #result = func(*args)
        #print(lst)
        result = list(args[::-1])
        return result
    return wrapper



@my_dec
def my_func(*args):
    my_list = []
    for i in args:
        my_list.append(i)
    return my_list


print(my_func(1,2,3,4,5,6,7,8,9,10))
