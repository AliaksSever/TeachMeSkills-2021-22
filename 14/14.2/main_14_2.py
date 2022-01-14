
import argparse
from datetime import datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument('-fn','--first-name',required=True)
parser.add_argument('-ln','--last-name',required=True)
parser.add_argument('-ft','--focusing_time',default=10,type=int)
parser.add_argument('-to','--time_out',default=5,type=int)
parser.add_argument('-ns','--cycles-number',default=4,type=int)
parser.add_argument('-tn','--task-name',default=None,type=str)
args = parser.parse_args()
print('First name:',args.first_name)
print('Last name:',args.last_name)
print('Focusing time:',args.focusing_time)
print('Time Out:',args.time_out)
print('The number of Cycles:',args.cycles_number)
print('Task name:',args.task_name)

with open('log_file.txt','a') as file:
    file.write(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S:")} - {args.first_name} {args.last_name}: '
               f'Task - {args.task_name}, Foc.Time - {args.focusing_time} min, Time Out - {args.time_out}, '
               f'Cycles - {args.cycles_number} \n')


'''work = args.focusing_time
while work != 0 and args.cycles_number != 0:
    print(f'You have {work} minutes to work!')
    time.sleep(1)
    work -= 1
    if work == 0 and args.cycles_number > 0:
        print(f'Pause! You have {args.time_out} minutes to rest')
        time.sleep(args.time_out)
        args.cycles_number -= 1
        work = args.focusing_time
print('End of Work!')'''

for i in range(args.cycles_number):
    work_time = args.focusing_time
    print(f'You have {args.cycles_number} cycles left!')
    while work_time != 0:
        print(f'You have {work_time} minutes to work!')
        time.sleep(1)
        work_time -= 1
        if work_time == 0:
            print(f'Pause! You have {args.time_out} minutes to rest')
            time.sleep(args.time_out)
    work_time = args.focusing_time
    args.cycles_number -= 1
print('End of Work!')