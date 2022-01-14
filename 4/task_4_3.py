dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print(dct)

dct_list = list(dct)
index = 0


# Способ 1. С помощью While
'''
while index<len(dct_list):
    dct_list[index] = dct_list[index]+str(len(dct_list[index]))
    dct[dct_list[index]] = dct.pop(list(dct)[0])
    index+=1
print(dct)
'''

# Способ 2. С помощью For
for key in dct_list:
    dct[key + str(len(key))] = dct.pop(key)
print(dct)