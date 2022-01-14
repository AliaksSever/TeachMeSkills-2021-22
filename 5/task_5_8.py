
st = input('Введите предложение: ')

tm = st.split(' ')

for i in range(len(tm)):
    tm[i] = tm[i][::-1]
    st = ' '.join(tm)
print(st)