from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

Session = sessionmaker(bind=engine)
session = Session()

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")
print("Las parroquias que tienen establecimientos únicamente en la jornada 'Matutina y Vespertina'\n")
consulta = session.query(Parroquia.nombre).join(Establecimiento).\
      filter(Establecimiento.jornada == "Matutina y Vespertina").distinct().all()

for parroquia in consulta:
    print(parroquia[0])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")
print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459\n")
estudiantes = [448, 450, 451, 454, 458, 459]

consulta_2 = session.query(Canton.nombre).join(Parroquia).join(Establecimiento).\
    filter(Establecimiento.parroquia_id == Parroquia.id,
           Parroquia.canton_id == Canton.id,
           Establecimiento.numEstud.in_(estudiantes)).distinct().all()

for canton in consulta_2:
    print(canton[0])


