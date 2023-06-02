from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

Session = sessionmaker(bind=engine)
session = Session()

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")

consulta = session.query(Establecimiento.id, Establecimiento.nombre).\
    join(Parroquia).filter(Parroquia.id == Establecimiento.parroquia_id,
           Establecimiento.numDocen > 40,
           Establecimiento.tipoEdu == "Educación regular").\
    order_by(Parroquia.nombre).\
    all()

for estable in consulta:
    print(estable[0], estable[1])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")

consulta2 = session.query(Establecimiento.id, Establecimiento.nombre).\
    order_by(Establecimiento.sostenimiento).\
    filter(Establecimiento.codDist!= "11D04").\
    all()

for estable1 in consulta2:
    print(estable1[0], estable1[1])