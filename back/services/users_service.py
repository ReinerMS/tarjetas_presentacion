from fastapi import HTTPException
from sqlalchemy import create_engine
from bd import DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from queries.users_queries import post_users, get_bd_users, check_email_query
from models.users_model import usersModel
from models.logs_models import logsModel
from services.logs_service import create_log


def get_users():
    # Crear el motor de conexión
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as test:
            # Hace la consulta a la base de datos con el Query
            result = test.execute(get_bd_users)
            
            # Obtiene los nombres de las columnas
            columns = result.keys()
            
            # Convierte cada fila en un diccionario {nombre_columna: valor}
            respuesta = [dict(zip(columns, row)) for row in result.fetchall()]

            return(respuesta)

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def post_bd_users(user:usersModel):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as post_Users:
            # Verificar si el email ya existe en la base de datos
            result = post_Users.execute(check_email_query, {"email": user.email})
            email_exists = result.scalar()  # Obtener el conteo

            if email_exists > 0:
                # Registrar el intento de creación de una tarjeta existente
                create_log(logsModel(change="Intento crear un usuario que ya existe", table="users", email= "rmoras@colonos.com"))
                
                raise HTTPException(status_code=400, detail="Usiario ya existe")
            
            # Crear un nuevo usuario si no existe el email
            post_Users.execute(post_users,{"name": user.name, 
                                           "email": user.email, 
                                           "lastName": user.lastName, 
                                           "company":user.company, 
                                           "password":user.password, 
                                           "status": user.status})
            create_log(logsModel(change="Creo un usuario un usuario", table="users", email= "rmoras@colonos.com"))
        return {"message": "Usuario agregado con éxito"}
        
    except SQLAlchemyError as e:
        print (f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=404, detail="Error al insertar en la base de datos")
