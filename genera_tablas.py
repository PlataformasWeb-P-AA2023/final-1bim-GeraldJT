from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codDivPolProv = Column(Integer)
    nombre = Column(String(100))
    # Mapea la relación entre las clases
    # por la llave foránea
    cantones = relationship("cantones", back_populates="provincias")

    
    def __repr__(self):
        return "Provincia: codigo de division politica:%d nombre=%s " % (
                          self.nombre, 
                          self.codDivPolitica)

class Canton(Base):
    __tablename__ = 'cantones'
    id = Column(Integer, primary_key=True)
    codDivPolCan = Column(Integer)
    nombre = Column(String(1000), nullable=False)
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    provincia = relationship("provincia", back_populate= "cantones")
    parroquias = relationship("parroquias", back_populates="cantones")
    
    def __repr__(self):
        return "Cantones: CodDivPolCan:%d  nombre:%s" % (
                self.codDivPolCan, self.nombre)

class Parroquia(Base):
    __tablename__ = 'Parroquias'
    id = Column(Integer, primary_key=True)
    codDivPolPar = Column(Integer)
    nombre = Column(String(1000), nullable=False)
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Mapea la relación entre las clases
    canton = relationship ("canton", back_populates= "parroquias")
    club  = relationship("Establecimientos", back_populates="Parroquias")
    
    def __repr__(self):
        return "Cantones: CodDivPolCan:%d  nombre:%s" % (
                self.codDivPolCan, self.nombre)

class Establecimiento(Base):
    __tablename__ = 'Establecimientos'
    id = Column(Integer, primary_key=True)
    codAMIE = Column(String(100))
    nombre = Column(String(1000), nullable=False)
    codDist = Column(String(100))
    sostenimiento = Column(String(100))
    tipoEdu = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    acceso = Column(String(100))
    numEstud = Column(Integer)
    numDocen = Column(Integer)
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))

    parroquia  = relationship( "Parroquias", back_populates= "Establecimientos")
Base.metadata.create_all(engine)









