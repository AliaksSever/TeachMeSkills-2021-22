
# Задание: Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

my_funk = lambda **kwargs: {key*2:value for key,value in kwargs.items()}
print(my_funk(b=4,a = 5))