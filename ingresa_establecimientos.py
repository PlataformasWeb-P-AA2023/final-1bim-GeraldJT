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
    provincia = Provincias(codAMIE = l[0], nombre = l[1], codDist = l[8], sostenimiento = l[9],tipoEdu = l[10], \
                            modalidad = l[11], jornada = l[12], acceso = l[13], numEstud = l[14],numDocen = l[15])
    print(l[2]) 

    session.add(provincia)

session.commit()
    
       
       
