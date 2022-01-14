
# Work16

# Создание подключения к postgresql через sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy.orm import backref

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'test'
DB_ECHO = True

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)


# Задание 16.01: Создать таблицу Учебной группы(Group) с помощью sqlalchemy.
# Группа характеризуется названием(name).

Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

#16.04: Создание таблицы ассоциации
association_table = Table('association', Base.metadata,
    Column('student_id',Integer,ForeignKey('student.id')),
    Column('book_id',Integer,ForeignKey('book.id'))
)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self,name):
        self.name = name

# Продолжение снизу

# Связь многие-к-одному(ForeignKey)
# Основная задача: привязка несколько сущностей к одной общей.
# Примеры: альбом и песни, футболисты и команда (многие футболисты - одна команда)

# CREATE TABLE artist(
# id INTEGER PRIMARY KEY,
# name TEXT
# );

# CREATE TABLE album(
# id INTEGER,
# name TEXT,
# artist_id INTEGER,
# FOREIGN KEY (artist_id) REFERENCES artist(id)
# );  #Объединение таблицы album и таблицы artist

# Задание 16.02:
# Создать таблицу Студент(Student) с помощью sqlalchemy.
# Студент характеризуется именем(firstname) и фамилией(lastname) и группой к которой он приурочен.
# Создать две группы. Добавить в каждую по три студента.


#МНОГИЕ-К-ОДНОМУ
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    group_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group = relationship('Group', foreign_keys='Student.group_id', backref='student')
    books = relationship('Student', secondary=association_table, backref='students') #16/04


    def __init__(self,name,lastname,group):
        self.name = name
        self.lastname = lastname
        self.group = group

# Base.metadata.create_all(engine)

# gr1 = Group("z61")
# gr2 = Group("z62")
#
# st1 = Student("Alex","Severin", group=gr1)
# st2 = Student("Arina","Kolots", group=gr1)
# st3 = Student("Ivan","Petrov", group=gr1)
#
# st4 = Student("Kostya","Sosnov", group=gr2)
# st5 = Student("Oleg","Ivanov", group=gr2)
# st6 = Student("Sergey","Adas", group=gr2)

# session.add_all([gr1, gr2, st1, st2, st3, st4, st5, st6])
# session.commit()


# Связь Один-к-одному (OneToOne)
# Основная задача - дробление большой таблицы(модели) на мелкие составляющие. (country - capital city)
# Пример: у одной столицы - одна страна, столица не может относиться ко многим странам

# CREATE TABLE booklet (
# id SERIAL NOT NULL,
# description VARCHAR,
# album_id INTEGER NOT NULL,
# PRIMARY KEY (id),
# FOREIGN KEY(album_id) REFERENCES album
# (id)
# )

# Задание 16.03: Создать таблицу Школьный дневник(Diary) с помощью sqlalchemy.
# Дневник характеризуется Средним баллом и студентом к которому он приурочен.

#ОДИН-К-ОДНОМУ
class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    average = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    student = relationship('Student', foreign_keys='Diary.student_id', backref=backref('diary', uselist=False))

    def __init__(self,average,student):
        self.average = average
        self.student = student

# Задание 16.04: Создать таблицу Книга(Book) с помощью sqlalchemy.
# Книга характеризуется названием, количеством страниц и студентами у которых эта книга.
# Создать 5 книг. Получить всех студентов и добавить каждому студенту эти пять книг.

#МНОГИЕ-КО-МНОГИМ
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages = Column(Integer)
    #students = relationship('Book',secondary=association_table,backref='books')

    def __init__(self,name,pages,students):
        self.name = name
        self.pages = pages
        self.students = students


Base.metadata.create_all(engine)


gr1 = Group("z61")
gr2 = Group("z62")


st1 = Student("Alex","Severin", group=gr1)
st2 = Student("Arina","Kolots", group=gr1)
st3 = Student("Ivan","Petrov", group=gr1)

st4 = Student("Kostya","Sosnov", group=gr2)
st5 = Student("Oleg","Ivanov", group=gr2)
st6 = Student("Sergey","Adas", group=gr2)


d1 = Diary(average=8, student=st1)
d2 = Diary(average=7, student=st2)
d3 = Diary(average=9, student=st3)
d4 = Diary(average=5, student=st4)
d5 = Diary(average=10, student=st5)
d6 = Diary(average=7, student=st6)

b1 = Book('Math',234,students=[st1,st2,st3])
b2 = Book('Programming',562,students=[st4,st5,st6])
# b1 = Book(name='Math',pages=234,students=[st1,st2,st3])
# b2 = Book(name='Programming',pages=562,students=[st4,st5,st6])


session.add_all([gr1, gr2, st1, st2, st3, st4, st5, st6, d1, d2, d3, d4, d5, d6,b1,b2])
session.commit()

# for i in b1.students:
#     print(i.name)
#print(st1.books)
#print(st1.group.name)
#print(st1.diary.average)
#print(st1.group.name)
#print(d6.student.lastname)


# Связь многие-ко-многим(ManyToMany):
# Основная задачи: связать множество одних сущностей с множеством других
# Пример: блюда и ингредиенты, студенты и книги.(таблица авторов(мн.число) и таблица книг разных авторов)

# CREATE TABLE track (
# id SERIAL NOT NULL,
# name VARCHAR,
# duration FLOAT,
# PRIMARY KEY (id)
# );
# CREATE TABLE association (
# album_id INTEGER,
# track_id INTEGER,
# FOREIGN KEY(album_id) REFERENCES album (id),
# FOREIGN KEY(track_id) REFERENCES track (id)
# )

# Задание 16.04: Создать таблицу Книга(Book) с помощью sqlalchemy.
# Книга характеризуется названием, количеством страниц и студентами у которых эта книга.
# Создать 5 книг. Получить всех студентов и добавить каждому студенту эти пять книг.

#МНОГИЕ-КО-МНОГИМ

# # 16.04: Создание таблицы ассоциации
# association_table = Table('association', Base.metadata,
#     Column('student.id',Integer,ForeignKey('student.id')),
#     Column('book_id',Integer,ForeignKey('book.id'))
# )

# class Book(Base):
#     __tablename__ = 'book'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     pages = Column(Integer)
#     students = relationship('Book',secondary=association_table,backref='books')
#
#     def __init__(self,name,pages,students):
#         self.name = name
#         self.pages = pages
#         self.students = students

