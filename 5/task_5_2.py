
chislo = (input('Введите число: '))
index = 0
su = 0
pr = 1



while index<len(chislo): # или for i in range(len(chislo)):
    su+=int(chislo[index])
    pr*=int(chislo[index])
    index+=1
print(f'{su} - сумма цифр')
print(f'{pr} - произведение цифр')
