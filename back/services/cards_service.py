from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError 
from sqlalchemy import create_engine
from bd import DATABASE_URL
from models.cards_model import cardModel, deleteModel, updateModel
from queries.cards_queries import post_card, get_bd_cards, delete_card_query, update_query, check_email_query
from services.logs_service import create_log
from models.logs_models import logsModel

def get_cards():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as cards:

            result = cards.execute(get_bd_cards)

            columns = result.keys()

            cards = [dict(zip(columns, row)) for row in result.fetchall()]
            
            return(cards)
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")



def create_cards(cards: cardModel):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as postCards:
            # Verificar si el email ya existe en la base de datos
            result = postCards.execute(check_email_query, {"email": cards.email})
            email_exists = result.scalar()  # Obtener el conteo

            if email_exists > 0:
                # Registrar el intento de creación de una tarjeta existente
                create_log(logsModel(change="Intento crear una tarjeta que ya existe", table="cards", email= "rmoras@colonos.com"))
                
                raise HTTPException(status_code=400, detail="La tarjeta ya existe")

            # Insertar nueva tarjeta si no existe el email
            postCards.execute(post_card, {"name": cards.name, 
                                          "lastName": cards.lastName, 
                                          "email": cards.email, 
                                          "company": cards.company, 
                                          "postName": cards.postName, 
                                          "socialNetwork1": cards.socialNetwork1, 
                                          "socialNetwork2": cards.socialNetwork2, 
                                          "socialNetwork3": cards.socialNetwork3, 
                                          "about": cards.about, 
                                          "photo": cards.photo, 
                                          "phone": cards.phone, 
                                          "wa": cards.wa,
                                          "areaCode": cards.areaCode})
            
            create_log(logsModel(change="Creo una tarjeta de presentacion", table="cards", email= "rmoras@colonos.com"))

        return {"message": "Card agregada con éxito"}

    except SQLAlchemyError as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")

    

def delete_card(card_delete: deleteModel):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as delete_email:
            result = delete_email.execute(delete_card_query, {"email": card_delete.email})
            create_log(logsModel(change="Elimino una tarjeta de presentación", table="cards", email= "rmoras@colonos.com"))
        return {"message": "Card eliminada con éxito"}
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al eliminar en la base de datos")
    


def update_card(updated_fields: updateModel):
    engine = create_engine(DATABASE_URL)
    
    # Extraemos los campos que no son None
    update_fields = {k: (v if v != '' else None) for k, v in updated_fields.dict().items() if v is not None}
        
    if not update_fields:
        raise HTTPException(status_code=400, detail="No hay campos para actualizar")

    # Agregamos valores por defecto para evitar errores si algún campo no se proporciona
    params = {
        "name": update_fields.get("name"),
        "lastName": update_fields.get("lastName"),
        "email": update_fields.get("email"),
        "company": update_fields.get("company"),
        "postName": update_fields.get("postName"),
        "socialNetwork1": update_fields.get("socialNetwork1"),
        "socialNetwork2": update_fields.get("socialNetwork2"),
        "socialNetwork3": update_fields.get("socialNetwork3"),
        "about": update_fields.get("about"),
        "photo": update_fields.get("photo"),
        "phone": update_fields.get("phone"),
        "wa": update_fields.get("wa"),
        "areaCode": update_fields.get("areaCode")
    }

    try:
        with engine.begin() as update_conn:
            result = update_conn.execute(update_query, params)
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="No se encontró ningun registro con ese email")
            create_log(logsModel(change="Actualizo una tarjeta de presentación", table="cards", email= "rmoras@colonos.com"))
        return {"message": "Card actualizada con éxito"}

    except SQLAlchemyError as e:
        print(f"Error al actualizar la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar la base de datos")
