
index_s = 0
index_f = 0

ls = [1,2,3,4,5,4,4,5,6,7,8,9,1,1,3,3,3,1,2,3,4,1]
tm = [] # тут сохраняем участки монотонности
print(ls)
print(len(ls))

for i in range(len(ls)-1):
    if ls[i]<ls[i+1]:
        if i + 1 == len(ls) - 1:
            index_f = i+1
            tm.append((index_s,index_f))
    else:
        if ls[i] > ls[i+1]:
            continue
        index_f=i # монотонное возрастание закончилось
        tm.append((index_s, index_f))
        index_s=i+1
print(tm)

print(len(tm))