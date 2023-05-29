
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData, Table
from configuracion import engine
from genera_tablas import Cantones
Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Parroquia

data = open("data/Listado-Instituciones-Educativas.csv", "r") 
lista = data.readlines()
lista = [l.replace(",", " ").split("|") for l in lista]
for l in lista:
    provincia = session.query(Cantones).filter_by(nombre=l[5]).one()  
    parroquia = Parroquia(codDivPolPar = l[6], nombre = l[7])
    metadata = MetaData(bind=engine)
    tabla = Table('parroquias', metadata, autoload=True)
    bus = tabla.select(parroquia.codDivPolPar)
    if bus != l[6]:
        session.add(parroquia)

session.commit()
    