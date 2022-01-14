
# Задание: Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε .
# С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε.

'''def fuct(n):
    fuct = 1
    for i in range(1,n+1):
        fuct*=i
    return fuct
print(fuct(7))'''

x = 3.14
e = 0.001
def fact(n): # Функция факториала
    if n<1:
        return 1
    return n*fact(n-1)

def element(n): # Функция элемента
    return ((-1)**n)*((x**(2*n+1))/fact(2*n+1))

def main():
    result = x
    n = 1
    while True:
        elem = element(n)
        if abs(elem) < e:
            break
        result+=element(n)
        n+=1
    print(result)

main()
