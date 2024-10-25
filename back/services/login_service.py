from fastapi import HTTPException
from sqlalchemy import create_engine ,text
from bd import DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from models.users_model import consultModel
from queries.users_queries import consult_bd_users

def consult_user(consult:consultModel):
     # Validación de campos vacíos
    if not consult.email or not consult.password:
        raise HTTPException(status_code=400, detail="El email y la contraseña son requeridos")
    
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as consult_user:
            result = consult_user.execute(consult_bd_users, {"email": consult.email, "password": consult.password})
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="No se encontró ningun registro con ese email")
        return {"message": "Si existe"}
        
    except SQLAlchemyError as e: # type: ignore
        print(f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")
