
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData, Table
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Provincias
# se crea un objetos de tipo Club
data = open("data/Listado-Instituciones-Educativas.csv", "r") 
lista = data.readlines()
lista = [l.replace(",", " ").split("|") for l in lista]
for l in lista:  
    provincia = Provincias(codDivPolProv = l[3], nombre = l[4])
    print(l[2]) 
    metadata = MetaData(bind=engine)
    tabla = Table('provincia', metadata, autoload=True)
    bus = tabla.select(provincia.codDivPolProv)
    if bus != l[3]:
        session.add(provincia)

session.commit()
    