from configuracion import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento



Session = sessionmaker(bind=engine)
session = Session()
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("consulta Nro.1 \n")
print("Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553\n")
consulta = session.query(Establecimiento.nombre).\
    join(Parroquia, Parroquia.codDivPolPar == 110553).\
    all()

for nombre in consulta:
    print(nombre[0])
print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro. 2\n")
print("Todos los establecimientos de la provincia del Oro\n")
consulta_2 = session.query(Establecimiento.nombre).\
    join(Parroquia).join(Canton).join(Provincia).\
    filter(Establecimiento.parroquia_id == Parroquia.id,
           Parroquia.canton_id == Canton.id,
           Canton.provincia_id == Provincia.id,
           Provincia.nombre == "EL ORO").\
    all()
for nombre1 in consulta_2:
    print(nombre1[0])

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")

print("Consulta Nro.3\n")
print("Todos los establecimientos del cantón de Portovelo\n")

consulta_3 = session.query(Establecimiento.nombre).join(Parroquia).join(Canton).\
    filter(Canton.nombre == "PORTOVELO").all()
for nombreIns in consulta_3:
    print(nombreIns[0])

print("-.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--\n\n")
print("Consulta Nro.4\n")
print("Todos los establecimientos del cantón de Zamora\n")
consulta_4 = session.query(Establecimiento.nombre).join(Parroquia).join(Canton).\
    filter(Canton.nombre == "ZAMORA").all()
for name in consulta_4:
    print(name[0])