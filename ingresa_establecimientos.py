from sqlalchemy.orm import sessionmaker
from configuracion import engine
import pandas as pd 
Session = sessionmaker(bind=engine)
session = Session()
from genera_tablas import Parroquia, Establecimiento

data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", delimiter="|") 

datosN = data.drop_duplicates(subset=['Código AMIE', 'Nombre de la Institución Educativa'])

print(datosN)
for  l, row in datosN.iterrows():
    codP= row['Código División Política Administrativa  Parroquia']
    print(codP)
    parroquia = session.query(Parroquia).filter_by(codDivPolPar=codP).one()
    codigoA = row['Código AMIE']
    nombreE = row['Nombre de la Institución Educativa']
    codigoD = row['Código de Distrito']
    sost = row['Sostenimiento']
    tipoE = row['Tipo de Educación']
    modalidad = row['Modalidad']
    jor= row['Jornada']
    acces= row['Acceso (terrestre/ aéreo/fluvial)']
    estud = row['Número de estudiantes']
    docen = row['Número de docentes']
    print(codigoA, nombreE,codigoD,sost,tipoE,modalidad,jor,acces,estud,docen)
    
    establecimiento = Establecimiento(codAMIE= codigoA, nombre=nombreE, codDist=codigoD,sostenimiento= sost, \
                                      tipoEdu = tipoE,modalidad= modalidad, jornada= jor, acceso =acces, \
                                          numEstud =estud, numDocen= docen, parroquias = parroquia)
    session.add(establecimiento)

session.commit()
