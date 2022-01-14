
import time
from datetime import datetime

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hr', '--hours', default=0, type=int)
parser.add_argument('-min', '--minutes', default=0, type=int)
parser.add_argument('-sec', '--seconds', default=10, type=int)
args = parser.parse_args()
print('First-name:',args.first_name)
print('Last_name:',args.last_name)
print('Hours:',args.hours)
print('Minutes:',args.minutes)
print('Seconds:',args.seconds)

with open('log.txt', 'a') as file:
    file.write(f'{datetime.now().strftime("%d.%m.%y %H:%M:%S")} - {args.first_name} {args.last_name}\n')
while args.hours or args.minutes or args.seconds:
    time_now = ''
    if args.hours <= 9:
        time_now += f'0{args.hours}'
    else:
        time_now+=f'{args.hours}'

    if args.minutes <= 9:
        time_now+=f':0{args.minutes}'
    else:
        time_now+=f':{args.minutes}'

    if args.seconds <= 9:
        time_now+=f':0{args.seconds}'
    else:
        time_now+=f':{args.seconds}'
    print(time_now)
    time.sleep(1)
    if args.seconds == 0 and args.minutes > 0:
        args.minutes -= 1
        args.seconds += 59
    elif args.seconds == 0 and args.minutes == 0 and args.hours > 0:
        args.hours -= 1
        args.minutes += 59
        args.seconds += 59
    else:
        args.seconds -= 1
else:
    print('ALARM!!!')
file.close()