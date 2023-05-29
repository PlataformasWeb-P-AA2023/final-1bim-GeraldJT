from sqlalchemy import create_engine
# este módulo será usado para posibles configuraciones
#
# cadena conector a la base de datos
#
# Sqlite
engine = create_engine("mysql+mysqlconnector://root:gerald@localhost:3306/demo1", echo=True)


# Mysql
# para el uso de este dialecto en SqlAlchemy
# instalar "pip install PyMySQL"
# cadena_base_datos = 'mysql+pymysql://usuario:clave@localhost/bd_name'
