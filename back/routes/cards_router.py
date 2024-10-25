from fastapi import APIRouter
from services.cards_service import get_cards, create_cards,delete_card, update_card, cardModel, deleteModel, updateModel
from models.logs_models import logsModel # Modelo de la tarjeta
from services.logs_service import create_log # Sesión de la base de datos

router = APIRouter()

@router.get("/")
def read_root():
    cards = get_cards()
    return(cards)

@router.post("/")
def create_root(cards:cardModel):
    message = create_cards(cards)
    return (message)

@router.delete("/")
def delete_card_endpoint(cards:deleteModel):
        message = delete_card(cards)
        create_log(logsModel(change = "Elimino una tarjeta de presentación", table = "cards", email = "rmoras@colonos.com" ))
        return (message)

@router.patch("/")
def update_card_endpoint(cards:updateModel):
        message = update_card(cards)
        create_log(logsModel(change = "Realizo una actualización de tarjeta de presentación", table = "cards", email = "rmoras@colonos.com" ))
        return (message)