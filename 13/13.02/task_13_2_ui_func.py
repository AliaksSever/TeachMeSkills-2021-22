import task_13_2_exception
import task_13_2_classes

def Process():
    while True:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        sing = input('Choose the operation: +,-,*,/ or 0 to stop: ')
        if sing == '0':
            break
        elif sing == '+':
            print(f'Answer: {task_13_2_classes.Math(a,b).summa()}')
        elif sing == '-':
            print(f'Answer: {task_13_2_classes.Math(a,b).dif()}')
        elif sing == '*':
            print(f'Answer: {task_13_2_classes.Math(a,b).mul()}')
        elif sing == '/':
            print(f'Answer: {task_13_2_classes.Math(a,b).div()}')
        else:
            raise task_13_2_exception.MyException

