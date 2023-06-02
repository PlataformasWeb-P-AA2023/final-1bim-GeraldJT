
from sqlalchemy import create_engine
# este módulo será usado para posibles configuraciones
#
# cadena conector a la base de datos
#
# Sqlite
engine = create_engine("mysql+pymysql://root:gerald@localhost/final01", echo=True)
#engine = create_engine("sqlite:///final01.db") 

# Mysql
# para el uso de este dialecto en SqlAlchemy
# instalar "pip install PyMySQL"
# cadena_base_datos = 'mysql+pymysql://usuario:clave@localhost/bd_name'
