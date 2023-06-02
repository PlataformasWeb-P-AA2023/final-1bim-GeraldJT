from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import Provincia
import pandas as pd 

Session = sessionmaker(bind=engine)
session = Session()


data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", delimiter="|") 

datosN = data.drop_duplicates(subset=['Código División Política Administrativa Provincia'])

print("hola")
for  l, row in datosN.iterrows():
    codigoP = row['Código División Política Administrativa Provincia']
    nombreP = row['Provincia']
    print(codigoP, nombreP)
    provincia = Provincia (codDivPolProv=int(codigoP), nombre=nombreP)
    session.add(provincia)

session.commit()
