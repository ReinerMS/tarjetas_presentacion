from fastapi import HTTPException
from sqlalchemy import create_engine
from bd import DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from queries.logs_queries import get_bd_logs, post_bd_logs
from models.logs_models import logsModel


def consult_bd_logs():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as consult_logs:
             result = consult_logs.execute(get_bd_logs)
             columns = result.keys()
             logs = [dict(zip(columns, row)) for row in result.fetchall()]

        return(logs)
        
    except SQLAlchemyError as e: # type: ignore
        print(f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")

def create_log(logs:logsModel):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as postLog:
            postLog.execute(post_bd_logs, {"email": logs.email, "table": logs.table, "change": logs.change})
        
    except SQLAlchemyError as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")