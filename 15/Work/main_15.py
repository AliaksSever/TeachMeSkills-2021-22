
# Задание:

# 1.Создать таблицу

#CREATE TABLE user (
#    id integer primary key autoincrement,
#    firstname varchar(255),
#    lastname varchar(255),
#    age integer
#)


# 2.Добавить 5 записей

#insert into user (firstname, lastname, age)
#values ('Alex','Sever',22),('Oleg','Ivanov',26),('Natasha','Kamluk',35),
#       ('Polina','Pashkevich',21),('Arina','Kolontsova',22)


# 3.Получить всех пользователей с вашим именем

#select * from user
#where firstname = 'Alex


# 4.Получить всех пользователей младше 25
#select * from user
#where age < 25



# 5.Получить всех пользователей в возрасте от 15 до 18
#select * from user
#where 15<age and age<18

# Выполнение запросов к базе с sqlalchemy
#from sqlalchemy import create_engine

#e = create_engine("sqlite:///test.db")
#e.execute("""
#create table user (
#id integer primary key autoincrement,
#firstname varchar,
#lastname varchar
#""")

# Добавление записей
#e = create_engine("sqlite:///test.db")
#e.execute("""
#insert into user (firstname, lastname)
#values ('Alex', 'Varkalov')
#""")

# Получение данных
#e = create_engine("sqlite:///test.db")
#result = e.execute("""select * from user""")
#for user in result:
#    print(user)



# ORM - Object related model
# Классический подход:
#1. Создаем объекты таблицы
#2. Создаем объекты БД
#3. Связываем объекты БД с классами с помощью ф-ции mapper()

'''from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///user1.db",echo=True)
metadata = MetaData()
user_table = Table('user',metadata,
    Column('id',Integer,primary_key=True),
    Column('firstname',String),
    Column('lastname',String)
)
metadata.create_all(engine)
class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
mapper(User,user_table)
user = User('Alex','Severin')'''

'''from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///user1.db",echo=True)
Base = declarative_base()
class Person(Base):
    __tablename__='person'
    id = Column(Integer,primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

Base.metadata.create_all(engine)
'''

