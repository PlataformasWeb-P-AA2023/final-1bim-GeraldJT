from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import Canton, Parroquia
import pandas as pd 
Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Canton

data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", delimiter="|") 

datosN = data.drop_duplicates(subset=['Código División Política Administrativa  Parroquia'])

print(datosN)
for  l, row in datosN.iterrows():
    codigoC = row['Código División Política Administrativa  Cantón']
    canton = session.query(Canton).filter_by(codDivPolCan =codigoC).one()
    codigoP = row['Código División Política Administrativa  Parroquia']
    nombreP = row['Parroquia']
    print(codigoP, codigoC, nombreP)
    parroquia = Parroquia(codDivPolPar=int(codigoP), nombre=nombreP, cantones=canton)
    session.add(parroquia)

session.commit()

    