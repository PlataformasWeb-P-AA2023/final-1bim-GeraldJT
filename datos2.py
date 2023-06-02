from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

Session = sessionmaker(bind=engine)
session = Session()

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")

consulta = session.query(Parroquia.nombre).join(Establecimiento).\
      filter(Establecimiento.jornada == "Matutina y Vespertina").distinct().all()

for parroquia in consulta:
    print(parroquia[0])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")

estudiantes = [448, 450, 451, 454, 458, 459]

consulta2 = session.query(Canton.nombre).\
    join(Parroquia).join(Establecimiento).filter(Establecimiento.parroquia_id == Parroquia.id,
           Parroquia.canton_id == Canton.id,
           Establecimiento.numEstud.in_(estudiantes)).\
    distinct().\
    all()

for canton in consulta2:
    print(canton[0])


