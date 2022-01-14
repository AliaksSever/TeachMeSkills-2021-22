# Задание:
# Создать таблицу продуктов.
# Атрибуты продукта: id,название,цена,количество,комментарий
# Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов
# Создать пользовательский интерфейс
# Примечание: все задание выполнить в нескольких файлах

# ДЕКЛАРАТИВНЫЙ ПОДХОД

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test15_1.db",echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    comment = Column(String)

    def __init__(self,name,price,quantity,comment):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.comment = comment


Base.metadata.create_all(engine)

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



# Интерфейс
v = int(input('To start enter 1, to stop - 0: '))
if v == 1:
    while True:
        v = int(input('Введите 1: Создание записи, 2: Чтение таблицы, 3: Обновление по id, 4: Удаление по id, 0: Выход. '))
        if v == 1:
            print("Вы выбрали 'Создание записи'")
            Create()
        elif v == 2:
            print("Вы выбрали 'Чтение таблицы'")
            Read()
        elif v == 3:
            print("Вы выбрали 'Обновление по id'")
            n = int(input('Введите id: '))
            Update_by_id(n)
        elif v == 4:
            print("Вы выбрали 'Удаление по id'")
            n = int(input('Введите id: '))
            Delete_by_id(n)
        elif v == 0:
            print('Вы вышли из программы')
            break
        else:
            print('Пожалуйста, выберете одно из предложенных значений')

