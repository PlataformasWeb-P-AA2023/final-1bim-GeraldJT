
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData, Table
from configuracion import engine
from genera_tablas import Provincia, Canton

Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Cantones
# se crea un objetos de tipo Club
data = open("data/Listado-Instituciones-Educativas.csv", "r") 
lista = data.readlines()
lista = [l.replace(",", " ").split("|") for l in lista]
for l in lista:
    provincia = session.query(Provincia).filter_by(nombre=l[3]).one()
    canton = session.query(Canton).filter_by(nombre=l[5]).one() 
    
    if canton is None:
        canton = Canton(codDivPolCan = l[4], nombre = l[5], provincia = provincia, 
        parroquias = parroquias)
        print(l[2]) 
        session.add(canton)

session.commit()
    
