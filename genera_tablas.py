from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


from configuracion import engine




Base = declarative_base()



class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codDivPolProv = Column(Integer)
    nombre = Column(String(100))
    cantones = relationship("Canton", back_populates="provincias")

    
    def __repr__(self):
        return "Provincia: codigo de division politica:%d nombre=%s " % (
                          self.codDivPolProv, 
                          self.cantones)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codDivPolCan = Column(Integer)
    nombre = Column(String(1000), nullable=False)
    provincia_id = Column(Integer, ForeignKey('provincia.id'))

    provincias = relationship("Provincia", back_populates= "cantones")
    parroquias = relationship("Parroquia", back_populates="cantones")
    
    def __repr__(self):
        return "Cantones: CodDivPolCan:%d  nombre:%s" % (
                self.codDivPolCan, self.nombre)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codDivPolPar = Column(Integer)
    nombre = Column(String(1000), nullable=False)
    canton_id = Column(Integer, ForeignKey('canton.id'))
    cantones = relationship ("Canton", back_populates= "parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquias")
    
    def __repr__(self):
        return "Parroquia: codDivPolPar:%d  nombre:%s" % (
                self.codDivPolPar, self.nombre)

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
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

    parroquias  = relationship( "Parroquia", back_populates= "establecimientos")

Base.metadata.create_all(engine)









