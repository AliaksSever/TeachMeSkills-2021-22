import task_13_1_func
import task_13_1_exception

def Process():
    while True:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        sing = input('Choose the operation: +,-,*,/ or 0 to stop: ')
        if sing == '0':
            break
        elif sing == '+':
            print(f'Answer: {task_13_1_func.summa(a,b)}')
        elif sing == '-':
            print(f'Answer: {task_13_1_func.dif(a,b)}')
        elif sing == '*':
            print(f'Answer: {task_13_1_func.mul(a,b)}')
        elif sing == '/':
            print(f'Answer: {task_13_1_func.div(a,b)}')
        else:
            raise task_13_1_exception.MyException

