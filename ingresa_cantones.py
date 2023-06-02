
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData, Table
from configuracion import engine
from genera_tablas import Provincia, Canton
import pandas as pd 
Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Canton

data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", delimiter="|") 

datosN = data.drop_duplicates(subset=['Código División Política Administrativa  Cantón'])

print(datosN)
for  l, row in datosN.iterrows():
    codigoP = row['Código División Política Administrativa Provincia']
    provincia = session.query(Provincia).filter_by(codDivPolProv =codigoP).one()
    codigoC = row['Código División Política Administrativa  Cantón']
    nombreC = row['Cantón']
    print(codigoP, codigoC, nombreC)
    canton = Canton(codDivPolCan=int(codigoC), nombre=nombreC, provincias=provincia)
    session.add(canton)

session.commit()

    
