from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.sql import text

from setting import (
    DATABASE,
    USER,
    PASSWORD,
    HOST,
)

URL = "mysql+pymysql://{}:{}@{}/{}".format(
    USER, PASSWORD, HOST, DATABASE
)

ENIGNE = create_engine(url=URL, echo=True)


class DBManager():

    def __init__(self, engine):
        self.engine: Engine = engine
        self.create_table()

    def create_table(self):
        with self.engine.connect() as session:
            request = text("""CREATE TABLE if not exists post (
                id INTEGER PRIMARY KEY auto_increment, 
                title VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                dollar VARCHAR(255) NOT NULL,
                som VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                uploaded VARCHAR(255) NOT NULL,
                views VARCHAR(255) NOT NULL,
                тип_предложения VARCHAR(255),
                безопасность VARCHAR(255),
                высота_потолков VARCHAR(255),
                балкон VARCHAR(255),
                входная_дверь VARCHAR(255),
                газ VARCHAR(255),
                дом VARCHAR(255),
                интернет VARCHAR(255),
                мебель VARCHAR(255),
                отопление VARCHAR(255),
                парковка VARCHAR(255),
                период_аренды VARCHAR(255),
                площадь VARCHAR(255),
                пол VARCHAR(255),
                разное VARCHAR(255),
                санузел VARCHAR(255),
                серия VARCHAR(255),
                состояние VARCHAR(255),
                телефон VARCHAR(255),        
                этаж VARCHAR(255)
                )
            """)
            session.execute(request)

    
MANAGER = DBManager(engine=ENIGNE)