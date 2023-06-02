from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

Session = sessionmaker(bind=engine)
session = Session()

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores\n")
consulta = session.query(Establecimiento.id, Establecimiento.nombre).\
    order_by(Establecimiento.numEstud).\
    filter(Establecimiento.numDocen > 100).\
    all()

for estable in consulta:
    print(estable[0], estable[1])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores\n")
consulta_2 = session.query(Establecimiento.id, Establecimiento.nombre).\
    filter(Establecimiento.numDocen > 100).order_by(Establecimiento.numDocen).\
    all()

for estable in consulta_2:
    print(estable[0], estable[1])