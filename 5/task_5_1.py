
x = int(input('Enter X: '))
y = int(input('Enter Y: '))

while True:
    sing = input('Enter +, –, /, *: ')
    if sing != '0':
        if sing == '+':
            print(x + y)
        elif sing == '-':
            print(x - y)
        elif sing == '/':
            if y != 0:
                print(int(x / y))
            else:
                print('На ноль делить нельзя!')
        elif sing == '*':
            print(x * y)

        else:
            print('Неверный знак операции')
    else:
        break