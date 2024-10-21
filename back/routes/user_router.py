from fastapi import APIRouter
from services.users_service import get_users, post_bd_users, usersModel
from services.logs_service import create_log
from models.logs_models import logsModel

router = APIRouter()

@router.get("/")
def read_root():
    users = get_users()
    return(users)

@router.post("/")
def users_root(users:usersModel):
    message = post_bd_users(users)
    return (message)