
#WORK

# Join
# JOIN - Операция соединения, предназначена для обеспечения выборки данных из двух таблиц
#и включения этих данных в один результирующий набор.

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'test5'

engine = create_engine(
f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)
    artist = relationship('Artist', foreign_keys='Album.artist_id', backref='albums')

Base.metadata.create_all(engine)

artist1 = Artist(name='Sunflower')
artist2 = Artist(name='Mushrooms')
artist3 = Artist(name='Trees')
album1 = Album(name='Only sun we love', artist=artist1)
album2 = Album(name='Only moon we love', artist=artist2)
album3 = Album(name='Only sun we love', artist=artist3)
# session.add_all([artist1, artist2, artist3, album1, album2, album3])
# session.commit()

# Join sqlalchemy

artists_albums = session.query(Artist, Album).join(
Album, Artist.id == Album.artist_id).filter(
Album.name == 'Only sun we love').all()

# Join sql
# создаем таблицу
# CREATE TABLE artist(
#     id INTEGER PRIMARY KEY,
#     name TEXT
# );
# CREATE TABLE album(
#     id INTEGER,
#     name TEXT,
#     artist_id INTEGER,
#     FOREIGN KEY (artist_id) REFERENCES artist(id)
# );

# заполняем таблицу

#artis
# INSERT into artist(id, name)
# VALUES (3,'Trees'); # и так 3 артистов

#album
# INSERT INTO album(id, name, artist_id)
# VALUES (1,'Only sun we love',1)

#Join sql
# SELECT *
# FROM artist JOIN album ON artist.id = album.artist_id
# WHERE album.name = 'Only sun we love';

# WORK
# CREATE TABLE basket_a(
#     id INTEGER PRIMARY KEY,
#     fruit VARCHAR (100) NOT NULL
# );
#
# CREATE TABLE basket_b(
#     id INTEGER PRIMARY KEY,
#     fruit VARCHAR (100) NOT NULL
# );

# INSERT INTO basket_a (id, fruit)
# VALUES
#     (1, 'Apple'),
#     (2, 'Orange'),
#     (3, 'Banana'),
#     (4, 'Cucumber');
#
# INSERT INTO basket_b (id, fruit)
# VALUES
#     (1, 'Orange'),
#     (2, 'Apple'),
#     (3, 'Watermelon'),
#     (4, 'Pear');


#Inner join (выбираем id и fruit из 2 таблиц где fruit совпадают)
# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# INNER JOIN basket_b b ON a.fruit = b.fruit;

#Left join
# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# LEFT JOIN basket_b b ON a.fruit = b.fruit

#Left outer join
# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# LEFT JOIN basket_b b ON a.fruit = b.fruit
# WHERE b.id IS NULL;

#Full outer join
# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# FULL OUTER JOIN basket_b b ON a.fruit
# = b.fruit;

#Full outer excluding join

# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# FULL JOIN basket_b b ON a.fruit = b.fruit
# WHERE a.id IS NULL OR b.id IS NULL;

# Cross join
# SELECT
#     a.id id_a,
#     a.fruit fruit_a,
#     b.id id_b,
#     b.fruit fruit_b
# FROM
#     basket_a a
# CROSS JOIN basket_b as b;