# Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



e = create_engine("sqlite:///test15_1.db")
Session = sessionmaker(bind=e)
session = Session()

# Создание записи:
def Create():
    n = input('name: ')
    p = int(input('price: '))
    q = int(input('quantity: '))
    c = input('comment: ')
    print(f'В таблицу будет добавлена следующая запись:\n {n} {p} {q} {c}\n Продолжить?(1/0)')
    variant = int(input('variant?: '))
    if variant == 0:
        print('Отмена записи.')
    else:
        session.add(Products(n,p,q,c))
        session.commit()
        print('Запись успешно добавлена')

# Чтение:
def Read():
    obj = session.query(Products.id, Products.name, Products.price, Products.comment).all()
    for i in obj:
        print(i)

# Обновление по id:
def Update_by_id(n):
    obj = session.query(Products).get(n)
    name = input('Введите новое значение name или enter, чтобы оставить прежнее: ')
    if name:
        obj.name = name
    price = input('Введите новое значение price или enter, чтобы оставить прежнее: ')
    if price:
        obj.price = int(price)
    quantity = input('Введите новое значение quantity или enter, чтобы оставить прежнее: ')
    if quantity:
        obj.quantity = quantity
    comment = input('Введите новое значение comment или enter, чтобы оставить прежнее: ')
    if comment:
        obj.comment = comment
    session.commit()

# Удаление по id:
def Delete_by_id(n):
    obj = session.query(Products).get(n)
    if obj:
        session.delete(obj)
        session.commit()
    else:
        print(f'В таблице отсутствует запись с id = {n}')