from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

Session = sessionmaker(bind=engine)
session = Session()

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")

docentes = [0, 5, 11]

consulta = session.query(Canton.id, Canton.nombre).join(Parroquia).join(Establecimiento).\
    filter(Establecimiento.parroquia_id == Parroquia.id,Parroquia.canton_id == Canton.id,
           Establecimiento.numDocen.in_(docentes)).distinct().all()

for canton in consulta:
    print(canton[0], canton[1])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")

consulta2 = session.query(Establecimiento.id, Establecimiento.nombre).join(Parroquia).\
    filter(Parroquia.id == Establecimiento.parroquia_id,
           Parroquia.nombre == "PINDAL",
           Establecimiento.numEstud >= 21).distinct().all()

for estable in consulta2:
    print(estable[0], estable[1])