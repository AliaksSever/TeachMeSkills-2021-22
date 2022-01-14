
# Создать таблицы Brand(name), Car(model,release_yerar,brand(foreing key на таблицу Brand)).
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для бренда и машины.
# Создать пользовательский интерфейс

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql.schema import ForeignKey

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'test1'
DB_ECHO = True

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


#МНОГИЕ-К-ОДНОМУ
class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey("brand.id"), nullable=False)
    brand = relationship("Brand", foreign_keys="Car.brand_id", backref="car")


    def __init__(self, model,release_year, brand):
        self.model = model
        self.release_year = release_year
        self.brand = brand

Base.metadata.create_all(engine)

b1 = Brand('BMW')
b2 = Brand('Audi')

# car1 = Car('tuareg', 2019, brand=b1)
#
# session.add_all([b1,car1])
# session.commit()
#
# print(car1.brand.name)

