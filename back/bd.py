
# Datos de conexión
usuario = "root"
contraseña = "admin"
host = "127.0.0.1"
base_datos = "tarjetasPresentacion"

# Crear la URL de conexión
DATABASE_URL = f"mysql+pymysql://{usuario}:{contraseña}@{host}/{base_datos}"