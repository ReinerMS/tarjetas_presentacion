from fastapi import HTTPException
from sqlalchemy import create_engine
from bd import DATABASE_URL
from sqlalchemy.exc import SQLAlchemyError
from models.company_model import Company
from queries.company_queries import get_bd_company, post_company


def get_company():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as company:

            result = company.execute(get_bd_company)

            columns = result.keys()

            company = [dict(zip(columns, row)) for row in result.fetchall()]

            return(company)
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def create_company(company:Company):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as postCompany:
            postCompany.execute(post_company, {"name": company.name, "img": company.img})
        return {"message": "Empresa agregada con éxito"}
        
    except SQLAlchemyError as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")
